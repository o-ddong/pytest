import pytest

def test_our_first_test() -> None:
    assert 1 == 1

def test_our_two_test() -> None:
    assert 1 == 2

@pytest.mark.skip
def test_our_three_test() -> None:
    assert 1 == 3

@pytest.mark.skipif(4 > 1, reason="Skipped because 4 > 1")
def test_our_three_test() -> None:
    """4 > 1이 참이므로 이 테스트는 SKIP하고 다음으로 넘어갑니다."""
    """False일 경우 테스트 진행 가능"""
    assert 1 == 3

"""
@pytest.mark.slow
pytest -v -p no:warnings -m slow -> slow 데코레이터가 붙은 애들 검사
pytest -v -p no:warnings -m "not slow" -> slow 데코데이터가 안붙은 애들 검사
"""
@pytest.mark.slow
def test_with_custom_mark1() -> None:
    pass

@pytest.mark.slow
def test_with_custom_mark2() -> None:
    pass


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"

"""
@pytest.fixture
fixture란 테스팅을 하는데 있어서 필요한 부분들을 혹은 조건들을 미리 준비해놓은 리소스 혹은 코드들을 의미
"""
@pytest.fixture
def company() -> Company:
    return Company(name="Fiver", stock_symbol="FVRR")

"""
pytest -v -p no:warnings -s -> 출력(print)까지 보고 싶다면 -s 포함
"""
def test_with_fixture(company: Company) -> None:
    print(f"Printing {company} from fixture")


"""
1. parametrize를 사용하려면 이를 사용하는 함수 또한 존재해야 하고
2. ids를 통해 네이밍을 해줄 수 있음
"""
@pytest.mark.parametrize(
    "company_name",
    ["Tictok", "Instargram", "Twitch"],
    ids=["TICTOK TEST", "INSTARGRAM TEST", "TWITCH TEST"],
)

def test_parametrized(company_name: str) -> None:
    print(f"\nTest with {company_name}")


"""
일부로 예외 발생시켜서 체크하는 Test
"""
def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")

def test_raise_covid19_exception_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)