__author__ = 'harsha'

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

