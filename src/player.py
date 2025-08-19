from src.settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, surface, groups, collision_sprites):
        super().__init__(groups)

        self.image = pygame.Surface((48, 56))
        self.image.fill('red')
        self.rect = self.image.get_frect(topleft=pos)
        self.old_rect = self.rect.copy()

        self.direction = vector(0, 0)
        self.speed = 200
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        input_vector = vector(0, 0)

        if keys[pygame.K_d]:
            input_vector.x += 1

        if keys[pygame.K_a]:
            input_vector.x -= 1

        # normalize keeps the direction of the vector but keeps same length.
        # a vector of (0,0) is invalid, hence the if statement
        self.direction = input_vector.normalize() if input_vector else input_vector

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def collision(self, axis):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    if self.rect.right >= sprite.rect.left and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.right = sprite.rect.left

                elif axis:
                    pass

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)

