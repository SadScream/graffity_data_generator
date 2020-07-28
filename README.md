# Sender
launch by run this command in cmd: ```python -m app``` or by running sender.bat

.\run\auth_config.py should contain variable `TOKEN` equals to your vk token with access to vk-api messages section

.\run\extra\addict_data.py should contain variable named `data` and type of dictionary.
This dictionary must contain field: 'path_to_img', 'path_to_audio', 'peers'
`path_to_img` and `path_to_audio` by default should be equals to `None`
`peers` is a dictonary of peers where keys are ids of peers(for example, 11 for conversation or 1234567 for dialog with user) and values are names of dialogs(i'm too lazy to automate this)