from core.commands import bot
from lisa.settings import TOKEN, __version__


if __name__ in '__main__':
  print('_____________________')
  print('LISA-Discord ')
  print(f'Version {__version__}')
  print('_____________________')

bot.run(TOKEN)