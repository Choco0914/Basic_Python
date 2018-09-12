# 임의의 키워드 매개변수 사용하기
def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만든다."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
"""
