class GameManager:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def checkCollision(self):
        for enemy in self.enemies:
            if enemy == self.player:
                continue

            if enemy.currentWeapon:
                for bullet in enemy.currentWeapon.bullets:
                    hit = playerBulletIntersection(self.player.rect, bullet)
                    if hit:
                        self.player.hit(enemy.currentWeapon.damage)
                        enemy.currentWeapon.bullets.pop(enemy.currentWeapon.bullets.index(bullet))

        for bullet in self.player.currentWeapon.bullets:
            for enemy in self.enemies:
                if enemy == self.player:
                    continue

                if playerBulletIntersection(enemy.rect, bullet):
                    self.player.currentWeapon.bullets.remove(bullet)


def playerBulletIntersection(rect, bullet):
    bulletCenter = (bullet.x + bullet.rad / 2, bullet.y + bullet.rad / 2)
    bulletDistanceX = abs(bulletCenter[0] - rect.centerx)
    bulletDistanceY = abs(bulletCenter[1] - rect.centery)
    if bulletDistanceX > rect.width / 2.0 + bullet.rad \
            or bulletDistanceY > rect.height / 2.0 + bullet.rad:
        return False
    if bulletDistanceX <= rect.width / 2.0 \
            or bulletDistanceY <= rect.height / 2.0:
        return True
    cornerX = bulletDistanceX - rect.width / 2.0
    cornerY = bulletDistanceY - rect.height / 2.0
    cornerDistanceSquare = cornerX ** 2.0 + cornerY ** 2.0
    return cornerDistanceSquare <= bullet.rad ** 2.0
