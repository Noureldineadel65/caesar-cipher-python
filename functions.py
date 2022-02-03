from string import ascii_letters


def range_alpha(start_letter, end_letter):
  return ascii_letters[
    ascii_letters.index(start_letter):ascii_letters.index(end_letter) + 1
  ]



 # def decode(message, shift):
 #     alphabet_list = list(range_alpha('a', 'Z'))
 #     message_list = list(message)
 #     new_message_list = []
 #     shifted_list = alphabet_list[shift:-1]
 #     post_shifted_list = alphabet_list[0:shift]
 #     for i in post_shifted_list:
 #         shifted_list.append(i)
 #     for i in message_list:
 #         if i in alphabet_list:
 #             new_message_list.append(shifted_list[alphabet_list.index(i)])
 #         else:
 #             new_message_list.append(i)
 #     return "".join(new_message_list)
 #
 # def encode(message, shift):
 #     alphabet_list = list(range_alpha('a', 'Z'))
 #     message_list = list(message)
 #     new_message_list = []
 #     shifted_list = alphabet_list[shift:-1]
 #     post_shifted_list = alphabet_list[0:shift]
 #     for i in post_shifted_list:
 #         shifted_list.append(i)
 #     for i in message_list:
 #         if i in alphabet_list:
 #             new_message_list.append(shifted_list[alphabet_list.index(i) - shift * 2])
 #         else:
 #             new_message_list.append(i)
 #     return "".join(new_message_list)

def cipher(type, message, shift):
     # Type is either "encode" or "decode"
     alphabet_list = list(range_alpha('a', 'Z'))
     message_list = list(message)
     new_message_list = []
     shifted_list = alphabet_list[shift:-1]
     post_shifted_list = alphabet_list[0:shift]
     for i in post_shifted_list:
         shifted_list.append(i)
     for i in message_list:
         if i in alphabet_list:
             if type == "encode":
                 new_message_list.append(shifted_list[alphabet_list.index(i)])
             elif type == "decode":
                 new_message_list.append(shifted_list[alphabet_list.index(i) - shift * 2])
         else:
             new_message_list.append(i)
     return "".join(new_message_list)
