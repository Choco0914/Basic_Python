# 연습문제 티셔츠
def make_shirt(size, message):
    print("\nThis " + message.title() + " shirt size is " + str(size))

make_shirt(90, 'ironmen')
make_shirt(message='야호우', size=105)

def make_shirt(size='L', message='I love Python'):
    print("\nThis " + message.title() + "shirt size is " + size.title())

make_shirt()
make_shirt(message='I love Django')
