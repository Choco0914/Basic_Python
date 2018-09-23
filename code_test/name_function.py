# 함수 테스트
def get_formatted_name(first, last, middle = ''):
    """읽기 좋은 전체 이름을 생성한다."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
