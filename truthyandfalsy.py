# truthy
print(bool('hello'))
print(bool(5))
# falsey
print(bool(''))
print(bool(0))
print(bool(None))

is_old = bool('Hello')
is_licensed = bool(5)

if is_old and is_licensed:
    print('You are old enough to drive and licensed.')
else:
    print('You are not of age.')

password = '123'
username = 'johnny'

if password and username:
    print('Login')
