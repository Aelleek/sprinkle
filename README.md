# sprinkle
Team Sprinkle Secretary Program Project





mongodb-community@4.2 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have mongodb-community@4.2 first in your PATH run:
  echo 'export PATH="/usr/local/opt/mongodb-community@4.2/bin:$PATH"' >> ~/.zshrc


To have launchd start mongodb/brew/mongodb-community@4.2 now and restart at login:
  brew services start mongodb/brew/mongodb-community@4.2
Or, if you don't want/need a background service you can just run:
  mongod --config /usr/local/etc/mongod.conf
