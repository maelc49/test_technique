class Tank:
    def __init__(self, armor, penetration, armor_type):
        self.armor = armor
        self.penetration = penetration
        self.armor_type = armor_type
        if armor_type not in ['chobham', 'composite', 'ceramic']:
            raise Exception('Invalid armor type %s' % (armor_type))
        self.tank = "Tank"

    def set_name(self, name):
        self.name = name

    def vulnerable(self, tank):
        real_armor = self.armor
        if self.armor_type == 'chobham':
            real_armor += 100
        else:
            real_armor += 50
        if real_armor <= tank.penetration:
            return True
        return False

    def swap_armor(self, othertank):
        self.armor, othertank.armor = othertank.armor, self.armor
        return othertank

    def __repr__(self):
        return self.name.lower().replace(' ', '-')


def test_tank_safe(shooter, test_vehicles=[]):
    for t in test_vehicles:
        if not t.vulnerable(shooter):
            print("A tank is safe")
            return True
    print("No tank is safe")
    return False


m1_1 = Tank(600, 670, 'chobham')
m1_2 = Tank(620, 670, 'chobham')
if m1_1.vulnerable(m1_2) is True:
    print('Vulnerable to tank m1_2')

m1_1.swap_armor(m1_2)
tanks = []
for i in range(5):
    #tanks.append(Tank(400, 400, 'steel')) # exception : steel isn't a valid armor type
    tanks.append(Tank(400, 400, 'composite'))
index = 0
for tank in tanks:
    tank.set_name('Tank' + str(index) + "_Small")
    index += 1
test = []

index = 0
while index < len(tanks):
    test.append(tanks[i].vulnerable(m1_1))
    index += 1

test_tank_safe(m1_1, tanks)
