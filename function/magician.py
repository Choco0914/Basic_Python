# 마술사
"""
마술사 이름으로 리스트를 만들자. 리스트에 있는 각 마술사 이름을 출력하는
show_magicians()함수에 리스트를 넘기자
"""

def show_magicians(magicians_name):
    """각 마술사 이름을 출력한다."""
    for magician in magicians_name:
        print(magician.title())

def make_great(magicians_name):
    """각 마술사 이름에 '훌륭한'이라는 구절을 붙여서 마술사 리스트를 수정한다."""
    while magicians_name:
        magician = magicians_name.pop()
        great = "great " + magician
        great_magician.append(great)

magicians_name = ['harry houdini', 'penn jilette and raymond teller'
    'david copperfield', 'apollo robbins', 'david devant']
great_magician = []
show_magicians(magicians_name)
make_great(magicians_name[:])

show_magicians(magicians_name)
show_magicians(great_magician)
