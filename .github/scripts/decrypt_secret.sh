#!/bin/sh

# Decrypt the file
# --batch to prevent interactive command
# --yes to assume "yes" for questions
gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE" \
--output $HOME/key/google_nlp_key.json $HOME/key/google_nlp_key.json.gpg

gpg --quiet --batch --yes --decrypt --passphrase="$LARGE_SECRET_PASSPHRASE_2" \
--output $HOME/key/twitter_key.json $HOME/key/twitter_key.json.gpg