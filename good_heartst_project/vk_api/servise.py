# import vk_api
# from vk_api.execute import VkFunction
#
# vk_get_wall_posts = VkFunction(args=('values',), code='''
#     return API.wall.get(%(values)s)['items'];
# ''')
#
# # vk_get_filtered = VkFunction(
# #     args=('method', 'values', 'key'),
# #     clean_args=('method', 'key'),  # аргументы будут сконвертированы через str
# #                                    # остальные через json.dumps
# #     code='''
# #     return API.%(method)s(%(values)s)["items"]@.%(key)s;
# # ''')
#
#
# def main():
#     # login, password =
#     vk_session = vk_api.VkApi(login, password)
#
#     try:
#         vk_session.auth(token_only=True)
#     except vk_api.AuthError as error_msg:
#         print(error_msg)
#         return
#
#     vk = vk_session.get_api()
#
#    data = vk_get_wall_post_ids(vk, {'domain': 'elista_kalmykia', 'count': 100})
#
#     print(data)
