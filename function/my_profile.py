"""
user_profile.py의 사본에서 시작하자 build_profile()을 호출해서 나 자신의 프로필을
만들자. 나의 성과 이름을 쓰고, 나에 관한 세 가지 키-값 쌍을 추가하자
"""
def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만든다."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return(profile)

my_profile = build_profile('jeongho', 'heo', age=27, location='Uiwang',
            job= 'programer')
print(my_profile)
