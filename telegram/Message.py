__author__ = 'harsha'

import telegram.User
import telegram.GroupChat
import telegram.Audio
import telegram.Document
import telegram.PhotoSize
import telegram.Location
import telegram.Contact
import telegram.Video
import telegram.Sticker

class Message(object):

    def __init__(self, message_id, from_user, date, chat, forward_from, forward_date, reply_to_message, text, audio,
                 document, photo, sticker, video, contact, location, new_chat_participant, left_chat_participant,
                 new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created):
        self.message_id = message_id
        self.from_user = from_user
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.text = text
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.contact = contact
        self.location = location
        self.new_chat_participant = new_chat_participant
        self.left_chat_participant = left_chat_participant
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created

    def __init__(self,jsonString):
        self.message_id = jsonString['message_id']
        self.date = jsonString['date']
        self.from_user = telegram.User.User(jsonString['from'])

        # Find out chat type
        chatType = jsonString['chat']
        if 'title' in chatType.keys():
            self.chat = telegram.GroupChat.GroupChat(jsonString['chat'])
        else:
            self.chat = telegram.User.User(jsonString['chat'])

        # Rest of the parameters are optional
        if 'forward_from' in jsonString.keys():
            self.forward_from = telegram.User.User(jsonString['forward_from'])
        else:
            self.forward_from = None

        if 'forward_date' in jsonString.keys():
            self.forward_date = int(jsonString['forward_date'])
        else:
            self.forward_date = None

        if 'reply_to_message' in jsonString.keys():
            self.reply_to_message = Message(jsonString['reply_to_message'])
        else:
            self.reply_to_message = None

        if 'text' in jsonString.keys():
            self.text = jsonString['text']
        else:
            self.text = ''

        if 'audio' in jsonString.keys():
            self.audio = telegram.Audio.Audio(jsonString['forward_from'])
        else:
            self.audio = None

        if 'document' in jsonString.keys():
            self.document = telegram.Document.Document(jsonString['document'])
        else:
            self.document = None

        if 'photo' in jsonString.keys():
            photoString = jsonString['photo']
            photoArray = []
            for i in range(0, len(photoString)):
                objPhoto = telegram.PhotoSize.PhotoSize(photoString[i])
                photoArray.append(objPhoto)
            self.photo = photoArray
        else:
            self.photo = None

        if 'sticker' in jsonString.keys():
            self.sticker = telegram.Sticker.Sticker(jsonString['sticker'])
        else:
            self.sticker = None

        if 'video' in jsonString.keys():
            self.video = telegram.Video.Video(jsonString['sticker'])
        else:
            self.video = None

        if 'contact' in jsonString.keys():
            self.contact = telegram.Contact.Contact(jsonString['contact'])
        else:
            self.contact = None

        if 'location' in jsonString.keys():
            self.location = telegram.Location.Location(jsonString['location'])
        else:
            self.location = None

        if 'new_chat_participant' in jsonString.keys():
            self.new_chat_participant = telegram.User.User(jsonString['new_chat_participant'])
        else:
            self.new_chat_participant = None

        if 'left_chat_participant' in jsonString.keys():
            self.left_chat_participant = telegram.User.User(jsonString['left_chat_participant'])
        else:
            self.left_chat_participant = None

        if 'new_chat_title' in jsonString.keys():
            self.new_chat_title = jsonString['new_chat_title']
        else:
            self.new_chat_title = None

        if 'new_chat_photo' in jsonString.keys():
            photoString = jsonString['new_chat_photo']
            photoArray = []
            for i in range(0, len(photoString)):
                objPhoto = telegram.PhotoSize.PhotoSize(photoString[i])
                photoArray.append(objPhoto)
            self.new_chat_photo = photoArray
        else:
            self.new_chat_photo = None

        if 'delete_chat_photo' in jsonString.keys():
            self.delete_chat_photo = bool(jsonString['delete_chat_photo'])
        else:
            self.delete_chat_photo = None

        if 'group_chat_created' in jsonString.keys():
            self.group_chat_created = bool(jsonString['group_chat_created'])
        else:
            self.group_chat_created = None

    def get_message_id(self):
        return self.message_id

    def get_from_user(self):
        return self.from_user

    def get_date(self):
        return self.date

    def get_chat(self):
        return self.chat

    def get_forward_from(self):
        return self.forward_from

    def get_forward_date(self):
        return self.forward_date

    def get_reply_to_message(self):
        return self.reply_to_message

    def get_text(self):
        return self.text

    def get_audio(self):
        return self.audio

    def get_document(self):
        return self.document

    def get_photo(self):
        return self.photo

    def get_sticker(self):
        return self.sticker

    def get_video(self):
        return self.video

    def get_contact(self):
        return self.contact

    def get_location(self):
        return self.location

    def get_new_chat_participant(self):
        return self.new_chat_participant

    def get_left_chat_participant(self):
        return self.left_chat_participant

    def get_new_chat_title(self):
        return self.new_chat_title

    def get_new_chat_photo(self):
        return self.new_chat_photo

    def get_delete_chat_photo(self):
        return self.delete_chat_photo

    def get_group_chat_created(self):
        return self.group_chat_created

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
