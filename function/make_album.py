def make_album(m_name, t_name, a_number=''):
    """음악가 이름과 앨범 타이틀을 받고 이들 정보가 들어 있는 딕셔너리를 반환한다"""
    album1 = {'name':'musician_name', 'title':'album_title'}
    if a_number:
        album1['a_number'] = a_number
    return album1

musician_album = make_album('marron5', 'v', a_number=1)
print(musician_album)

musician_album2 = make_album('jessie j', 'Pitch Perfect 2', a_number=3)
print(musician_album2)

musician_album3 = make_album('ed Sheeran', '÷', a_number=13)
print(musician_album3)

while True:
    print("\nPlease tell me musician name, album title" +
    " and Number of songs in album")
    print("(enter 'q' at any time to quit)")

    m_name = input("\nMusician name: ")
    if m_name == 'q':
        break
    t_name = input("\nTitle name: ")
    if t_name == 'q':
        break
    a_number = input("\n Number of songs in album: ")
    if a_number == 'q':
        break
    song = make_album(m_name, t_name, a_number)
    print("\n" + str(song))
