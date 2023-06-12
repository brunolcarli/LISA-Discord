from core.commands import client
from lisa.settings import TOKEN, __version__, ENV_REF
from core.keep_alive import keep_alive

if __name__ in '__main__':
  print('_____________________')
  print('LISA-Discord ')
  print(f'Version {__version__}')
  print('_____________________')

  if ENV_REF == 'replit':
    keep_alive()

  client.run(TOKEN)