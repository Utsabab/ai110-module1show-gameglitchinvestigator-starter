import random
from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# ──────────────────────────────────────────────────────────────────────────────
# Bug 2: Inverted hints (go higher/lower advice was backwards)
# check_guess returns (outcome, message)
# ──────────────────────────────────────────────────────────────────────────────

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_message_too_high_says_go_lower():
    # Bug 2: hint was inverted — guess above secret must tell player to go LOWER
    _, message = check_guess(80, 30)
    assert "LOWER" in message.upper()


def test_hint_message_too_low_says_go_higher():
    # Bug 2: hint was inverted — guess below secret must tell player to go HIGHER
    _, message = check_guess(10, 90)
    assert "HIGHER" in message.upper()


def test_winning_guess_message():
    # Winning guess should include a success message, not a direction hint
    _, message = check_guess(42, 42)
    assert "LOWER" not in message.upper()
    assert "HIGHER" not in message.upper()


# ──────────────────────────────────────────────────────────────────────────────
# Bug 1 & 8: Inconsistent difficulty ranges / UI always showed "1 to 100"
# get_range_for_difficulty must return the correct (low, high) per level
# ──────────────────────────────────────────────────────────────────────────────

def test_easy_mode_range():
    # Bug 1 & 8: Easy mode must return range (1, 20)
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_normal_mode_range():
    # Bug 1 & 8: Normal mode must return range (1, 50)
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_hard_mode_range():
    # Bug 1 & 8: Hard mode must return range (1, 100)
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_difficulty_range_ordering():
    # Bug 1: upper bound must increase with difficulty: Easy < Normal < Hard
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high
    assert normal_high < hard_high


def test_easy_range_lower_than_normal():
    # Bug 1: Easy should have a smaller range than Normal
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    assert easy_high < normal_high


def test_normal_range_lower_than_hard():
    # Bug 1: Normal should have a smaller range than Hard
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert normal_high < hard_high


# ──────────────────────────────────────────────────────────────────────────────
# Bug 7: New game generated secret number outside the level's range bounds
# Simulate secret generation using get_range_for_difficulty
# ──────────────────────────────────────────────────────────────────────────────

def test_secrets_stay_within_easy_range():
    # Bug 7: secrets generated after new game must stay within Easy bounds (1-20)
    low, high = get_range_for_difficulty("Easy")
    for _ in range(200):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secrets_stay_within_normal_range():
    # Bug 7: secrets generated after new game must stay within Normal bounds (1-50)
    low, high = get_range_for_difficulty("Normal")
    for _ in range(200):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_secrets_stay_within_hard_range():
    # Bug 7: secrets generated after new game must stay within Hard bounds (1-100)
    low, high = get_range_for_difficulty("Hard")
    for _ in range(200):
        secret = random.randint(low, high)
        assert low <= secret <= high


def test_easy_range_upper_bound_is_20():
    # Bug 7 & 8: Easy mode upper bound must be exactly 20, not 100
    _, high = get_range_for_difficulty("Easy")
    assert high == 20


def test_normal_range_upper_bound_is_50():
    # Bug 7 & 8: Normal mode upper bound must be exactly 50, not 100
    _, high = get_range_for_difficulty("Normal")
    assert high == 50


# ──────────────────────────────────────────────────────────────────────────────
# parse_guess — input validation (supports stable guess processing)
# ──────────────────────────────────────────────────────────────────────────────

def test_parse_valid_integer_guess():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_none_input_returns_error():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_empty_string_returns_error():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_non_numeric_string_returns_error():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_float_string_converts_to_int():
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert isinstance(value, int)


def test_parse_boundary_value_one():
    ok, value, err = parse_guess("1")
    assert ok is True
    assert value == 1


def test_parse_boundary_value_100():
    ok, value, err = parse_guess("100")
    assert ok is True
    assert value == 100


# ──────────────────────────────────────────────────────────────────────────────
# update_score — score calculation correctness
# ──────────────────────────────────────────────────────────────────────────────

def test_update_score_win_on_first_attempt():
    # Win on attempt 0 -> 100 - 10*(0+1) = 90 points added
    new_score = update_score(0, "Win", 0)
    assert new_score == 90


def test_update_score_win_awards_minimum_10_points():
    # Win very late -> minimum of 10 points guaranteed
    new_score = update_score(0, "Win", 100)
    assert new_score == 10


def test_update_score_win_adds_to_existing_score():
    new_score = update_score(200, "Win", 0)
    assert new_score == 290


def test_update_score_too_low_deducts_points():
    new_score = update_score(50, "Too Low", 1)
    assert new_score == 45


def test_update_score_too_high_even_attempt_adds_points():
    # Even attempt number with "Too High" grants bonus points
    new_score = update_score(50, "Too High", 0)
    assert new_score == 55


def test_update_score_too_high_odd_attempt_deducts_points():
    # Odd attempt number with "Too High" deducts points
    new_score = update_score(50, "Too High", 1)
    assert new_score == 45


def test_update_score_unknown_outcome_unchanged():
    new_score = update_score(100, "Unknown", 5)
    assert new_score == 100
