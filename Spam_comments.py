try:
    import time,requests,re,os
    from colorama import Fore
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install re')
    print('\n[+] Done')
def Error():
    while True:
        break
    print("[!!] THE TOOL IS STOP (RENEW THE SESSION ID'S)")
def sessid3():
    error=0
    use_comen = open('sids.txt', "r").read().splitlines()
    sid3=use_comen[1]
    done=0
    print(".......................")
    print("{USEING ANOTHER SESSION ID NOW..}")
    print(".......................")
    url=f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6965670367281858049&region=SA&priority_region=KW&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0 (Windows)&browser_online=true&verifyFp=verify_kqj9kjg8_h6I0T7wu_Rewg_4N6a_ANgb_RwrZSHwKIbIO&app_language=ar&timezone_name=Asia/Riyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=8&aweme_id={postid}&text={tx}&_signature=_02B4Z6wo00101Ue0rDwAAIDAxtrPJvZZqvFHtaiAADE0f6"
    headers={
        'Host': 'www.tiktok.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'tt-csrf-token': 'CNr_U36JufpaLA8R6x3M7GkU',
        'Origin': 'https://www.tiktok.com',
        'Referer': f'https://www.tiktok.com/@1v/video/{postid}?lang=ar&is_copy_url=1&is_from_webapp=v1',
        'Connection': 'keep-alive',
        'Cookie': f'tt_webid_v2=6965670367281858049; tt_webid=6965670367281858049; MONITOR_WEB_ID=6965670367281858049; _abck=DF7A347900A8D8FED81AFD5EE12008C7~-1~YAAQdjNWsl1zzyN6AQAAD7cyXAZ3nfriDtuXdGAv9Mmo32Q3hLhQ4r/uKlhg0feMz3cqNgX9hEFRY6NeifESz4/d7Zp5qfjYRFyd7yDwsIH0ny/d0SbuzqJlUu8CAklDceZg6m1ysoTZWYKhBypFJCzYnQgwhJzDhsw4IJc6H95DKPXQ24ih6mLTcDVJWvMdHrp1rgO4rDAMjCIwVZ8wezC1yX3UjDgPbcC72LZ5QQlydFlqSbsPVN0uFwyuMk7nfNYnIrmxliZG4ZyYYdfkMSFEMzXmU7pwklF77mMGCcHfWm6oHBS93JvstxlenJ0jkZ+x8Tj792R4Ei+ekZ3IDLbCHUt3/lKftAQGJilJ6Tt/9y/phesixXkfR/xyIHf7zMOf9XSbRZhRcWk=~-1~-1~-1; ttwid=1%7CGgSBNxhEX3SRZ-8gRwj6trJuRqBn9FTPhb-bLV09ikY%7C1625044649%7Ca0b4ef69542791d29f95f221bec9f060a3605bdf0cd6fda06c9243ed24f5719a; passport_csrf_token=f04fc476081a3d063b607f520e64780c; passport_csrf_token_default=f04fc476081a3d063b607f520e64780c; store-idc=alisg; store-country-code=kw; cmpl_token=AgQQAPOvF-RMpbCWRisot104-sqReLfT_4M0YP7d2Q; sid_guard={sid3}%7C1624784625%7C5184000%7CThu%2C+26-Aug-2021+09%3A03%3A45+GMT; uid_tt=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; uid_tt_ss=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; sid_tt={sid3}; sessionid={sid3}; sessionid_ss={sid3}; odin_tt=8dd8f35beed30aac4146eb6e04127df54b4f1cf2baaadce4ebc8cdcba4f1a6c41a236fff1ce54a20ddb30b9f17d50c0aa7b58403762896ca8ac3a39c019b7001f6d142bc93a3757420431d79d2b6bc1c; tt_csrf_token=CNr_U36JufpaLA8R6x3M7GkU; passport_fe_beating_status=true; R6kq3TV7=AE2gMlx6AQAAvYTIxl1fM6CJucIyAsBAUzGr4wnMSMq_6yiMDSgTUmhFcSbf|1|0|b3a2973dfcb43ae52d9d00e9277d1a6322c89558; csrf_session_id=fa5fdc18618e46b194f075f56bcae4bb; bm_sz=F0C984664CBD3F98CB69CC3A5D7311D7~YAAQdjNWslxzzyN6AQAAD7cyXAxHYhY8U5I2hd7pyliCaDNgsuAGvrdk20NPdnHcCgfuoQ4jTt9grk2oytGVbW5tLSYfrhXY3YvP1QNF6aamZaoqmem4EdYBQ9MB7WwprJmH3VhLP8rA8oNNKWu+kcnyP7wPW1zIWDsNXzUn0xo6rVLuPi7SqZI2wES/OECk; ak_bmsc=FAB809A889BE0FD52793A9AFE944C5E7~000000000000000000000000000000~YAAQdjNWsl5zzyN6AQAAD7cyXAyCowossZhpYTS17Hr59PNFrcXTcDFryYYdokg3LpNXsgKzh1XPNtNyQPIaBpTObs+sRSYDommrQqfkj+rmJXmJ9ZgGG9nmz9g+na9QQvlE1WCChZXDfqjafulwVYqiREPUGZOOYZQR+VFcscgiEIDX8Sf/oVd4y/DFai5cVmE+NdFv8mScSPqrnx7GN6aRjgNcH1U4AH2s5rDsXx8HFPeAx3Tv+GnXIe+LW4VkayVwC0jmsc/5ItiIBg/frNY6TGlhMC2GpkC/5r3kusXk7pGrOZ3guS4XutcnrywaEVBJ2mAT4HZMO4BGWGdQKuewF2jloIzCXLIMrEZZH/cn5YpzHY2bSMAOMcn5i2LGSnbgBwd5Gepl; bm_sv=DEBE6CA7A7EB283E553319561E46F9DD~RZAdeW6TH0kHw11O3hwiJna+CzGbn2Uq0XJUyTGiSWUjhw3nZNKxa7ykll7CbirsQfI9gqLMNlqF/UxaDjD2dEqXktEXKFSM7Bc850t9Kj8Q3Y3pX0/GQSdjYx0/15QSfNX8ueYzHrsYeiYz9ZXmGe+OUh1uYKw8zShfTUs4pBQ=; s_v_web_id=verify_kqj9kjg8_h6I0T7wu_Rewg_4N6a_ANgb_RwrZSHwKIbIO',
        'Content-Length': '0', }
    while True:
        time.sleep(6.6)
        req = requests.post(url, headers=headers)
        if '"تم إرسال التعليق بنجاح"' in req.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            done+=1
        elif 'أنت تعلق بسرعة كبيرة. خذ قسطًا من الراحة!' in req.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            error+=1
        elif 'انتهت صلاحية تسجيل الدخول' in req.text:
            print(f'\n\t[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱\nsession id [{sid3}]')
            Error()
            break
        elif '{}' in req.text:
            print(f'\n\t[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱\nsession id [{sid3}]')
            Error()
            break
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            error+=1
def sessid2():
    use_comen=open('sids.txt', "r").read().splitlines()
    sid2=use_comen[0]
    done=0
    error=0
    print(".......................")
    print("{USEING ANOTHER SESSION ID NOW..}")
    print(".......................")
    url = f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6965670367281858049&region=SA&priority_region=KW&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0 (Windows)&browser_online=true&verifyFp=verify_kqj9kjg8_h6I0T7wu_Rewg_4N6a_ANgb_RwrZSHwKIbIO&app_language=ar&timezone_name=Asia/Riyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=8&aweme_id={postid}&text={tx}&_signature=_02B4Z6wo00101Ue0rDwAAIDAxtrPJvZZqvFHtaiAADE0f6"
    headers = {
        'Host': 'www.tiktok.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'tt-csrf-token': 'CNr_U36JufpaLA8R6x3M7GkU',
        'Origin': 'https://www.tiktok.com',
        'Referer': f'https://www.tiktok.com/@1v/video/{postid}?lang=ar&is_copy_url=1&is_from_webapp=v1',
        'Connection': 'keep-alive',
        'Cookie': f'tt_webid_v2=6965670367281858049; tt_webid=6965670367281858049; MONITOR_WEB_ID=6965670367281858049; _abck=DF7A347900A8D8FED81AFD5EE12008C7~-1~YAAQdjNWsl1zzyN6AQAAD7cyXAZ3nfriDtuXdGAv9Mmo32Q3hLhQ4r/uKlhg0feMz3cqNgX9hEFRY6NeifESz4/d7Zp5qfjYRFyd7yDwsIH0ny/d0SbuzqJlUu8CAklDceZg6m1ysoTZWYKhBypFJCzYnQgwhJzDhsw4IJc6H95DKPXQ24ih6mLTcDVJWvMdHrp1rgO4rDAMjCIwVZ8wezC1yX3UjDgPbcC72LZ5QQlydFlqSbsPVN0uFwyuMk7nfNYnIrmxliZG4ZyYYdfkMSFEMzXmU7pwklF77mMGCcHfWm6oHBS93JvstxlenJ0jkZ+x8Tj792R4Ei+ekZ3IDLbCHUt3/lKftAQGJilJ6Tt/9y/phesixXkfR/xyIHf7zMOf9XSbRZhRcWk=~-1~-1~-1; ttwid=1%7CGgSBNxhEX3SRZ-8gRwj6trJuRqBn9FTPhb-bLV09ikY%7C1625044649%7Ca0b4ef69542791d29f95f221bec9f060a3605bdf0cd6fda06c9243ed24f5719a; passport_csrf_token=f04fc476081a3d063b607f520e64780c; passport_csrf_token_default=f04fc476081a3d063b607f520e64780c; store-idc=alisg; store-country-code=kw; cmpl_token=AgQQAPOvF-RMpbCWRisot104-sqReLfT_4M0YP7d2Q; sid_guard={sid2}%7C1624784625%7C5184000%7CThu%2C+26-Aug-2021+09%3A03%3A45+GMT; uid_tt=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; uid_tt_ss=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; sid_tt={sid2}; sessionid={sid2}; sessionid_ss={sid2}; odin_tt=8dd8f35beed30aac4146eb6e04127df54b4f1cf2baaadce4ebc8cdcba4f1a6c41a236fff1ce54a20ddb30b9f17d50c0aa7b58403762896ca8ac3a39c019b7001f6d142bc93a3757420431d79d2b6bc1c; tt_csrf_token=CNr_U36JufpaLA8R6x3M7GkU; passport_fe_beating_status=true; R6kq3TV7=AE2gMlx6AQAAvYTIxl1fM6CJucIyAsBAUzGr4wnMSMq_6yiMDSgTUmhFcSbf|1|0|b3a2973dfcb43ae52d9d00e9277d1a6322c89558; csrf_session_id=fa5fdc18618e46b194f075f56bcae4bb; bm_sz=F0C984664CBD3F98CB69CC3A5D7311D7~YAAQdjNWslxzzyN6AQAAD7cyXAxHYhY8U5I2hd7pyliCaDNgsuAGvrdk20NPdnHcCgfuoQ4jTt9grk2oytGVbW5tLSYfrhXY3YvP1QNF6aamZaoqmem4EdYBQ9MB7WwprJmH3VhLP8rA8oNNKWu+kcnyP7wPW1zIWDsNXzUn0xo6rVLuPi7SqZI2wES/OECk; ak_bmsc=FAB809A889BE0FD52793A9AFE944C5E7~000000000000000000000000000000~YAAQdjNWsl5zzyN6AQAAD7cyXAyCowossZhpYTS17Hr59PNFrcXTcDFryYYdokg3LpNXsgKzh1XPNtNyQPIaBpTObs+sRSYDommrQqfkj+rmJXmJ9ZgGG9nmz9g+na9QQvlE1WCChZXDfqjafulwVYqiREPUGZOOYZQR+VFcscgiEIDX8Sf/oVd4y/DFai5cVmE+NdFv8mScSPqrnx7GN6aRjgNcH1U4AH2s5rDsXx8HFPeAx3Tv+GnXIe+LW4VkayVwC0jmsc/5ItiIBg/frNY6TGlhMC2GpkC/5r3kusXk7pGrOZ3guS4XutcnrywaEVBJ2mAT4HZMO4BGWGdQKuewF2jloIzCXLIMrEZZH/cn5YpzHY2bSMAOMcn5i2LGSnbgBwd5Gepl; bm_sv=DEBE6CA7A7EB283E553319561E46F9DD~RZAdeW6TH0kHw11O3hwiJna+CzGbn2Uq0XJUyTGiSWUjhw3nZNKxa7ykll7CbirsQfI9gqLMNlqF/UxaDjD2dEqXktEXKFSM7Bc850t9Kj8Q3Y3pX0/GQSdjYx0/15QSfNX8ueYzHrsYeiYz9ZXmGe+OUh1uYKw8zShfTUs4pBQ=; s_v_web_id=verify_kqj9kjg8_h6I0T7wu_Rewg_4N6a_ANgb_RwrZSHwKIbIO',
        'Content-Length': '0', }
    while True:
        time.sleep(6.6)
        req = requests.post(url, headers=headers)
        if '"تم إرسال التعليق بنجاح"' in req.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            done += 1
        elif 'أنت تعلق بسرعة كبيرة. خذ قسطًا من الراحة!' in req.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            error+=1
        elif 'انتهت صلاحية تسجيل الدخول' in req.text:
            print(f'\n\t[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱\nsession id [{sid2}]')
            sessid3()
            break
        elif '{}' in req.text:
            print(f'\n\t[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱\nsession id [{sid2}]')
            sessid3()
            break
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            error+=1
def sessid1():
    global tx,postid
    error=0
    done=0
    tx=input("Enter Your text: ")
    postid=input("Enter the post id: ")
    print(".......................")
    sid1=input("session id: ")
    print(".......................")
    url = f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6965670367281858049&region=SA&priority_region=KW&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0 (Windows)&browser_online=true&verifyFp=verify_kqj9kjg8_h6I0T7wu_Rewg_4N6a_ANgb_RwrZSHwKIbIO&app_language=ar&timezone_name=Asia/Riyadh&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=8&aweme_id={postid}&text={tx}&_signature=_02B4Z6wo00101Ue0rDwAAIDAxtrPJvZZqvFHtaiAADE0f6"
    headers = {
        'Host': 'www.tiktok.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'tt-csrf-token': 'CNr_U36JufpaLA8R6x3M7GkU',
        'Origin': 'https://www.tiktok.com',
        'Referer': f'https://www.tiktok.com/@1v/video/{postid}?lang=ar&is_copy_url=1&is_from_webapp=v1',
        'Connection': 'keep-alive',
        'Cookie': f'tt_webid_v2=6965670367281858049; tt_webid=6965670367281858049; MONITOR_WEB_ID=6965670367281858049; _abck=DF7A347900A8D8FED81AFD5EE12008C7~-1~YAAQdjNWsl1zzyN6AQAAD7cyXAZ3nfriDtuXdGAv9Mmo32Q3hLhQ4r/uKlhg0feMz3cqNgX9hEFRY6NeifESz4/d7Zp5qfjYRFyd7yDwsIH0ny/d0SbuzqJlUu8CAklDceZg6m1ysoTZWYKhBypFJCzYnQgwhJzDhsw4IJc6H95DKPXQ24ih6mLTcDVJWvMdHrp1rgO4rDAMjCIwVZ8wezC1yX3UjDgPbcC72LZ5QQlydFlqSbsPVN0uFwyuMk7nfNYnIrmxliZG4ZyYYdfkMSFEMzXmU7pwklF77mMGCcHfWm6oHBS93JvstxlenJ0jkZ+x8Tj792R4Ei+ekZ3IDLbCHUt3/lKftAQGJilJ6Tt/9y/phesixXkfR/xyIHf7zMOf9XSbRZhRcWk=~-1~-1~-1; ttwid=1%7CGgSBNxhEX3SRZ-8gRwj6trJuRqBn9FTPhb-bLV09ikY%7C1625044649%7Ca0b4ef69542791d29f95f221bec9f060a3605bdf0cd6fda06c9243ed24f5719a; passport_csrf_token=f04fc476081a3d063b607f520e64780c; passport_csrf_token_default=f04fc476081a3d063b607f520e64780c; store-idc=alisg; store-country-code=kw; cmpl_token=AgQQAPOvF-RMpbCWRisot104-sqReLfT_4M0YP7d2Q; sid_guard={sid1}%7C1624784625%7C5184000%7CThu%2C+26-Aug-2021+09%3A03%3A45+GMT; uid_tt=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; uid_tt_ss=560c663051ee8ff8a3ff0068cf8eb4b98b29b305eedc84c15ca18d6869be8951; sid_tt={sid1}; sessionid={sid1}; sessionid_ss={sid1}; odin_tt=8dd8f35beed30aac4146eb6e04127df54b4f1cf2baaadce4ebc8cdcba4f1a6c41a236fff1ce54a20ddb30b9f17d50c0aa7b58403762896ca8ac3a39c019b7001f6d142bc93a3757420431d79d2b6bc1c; tt_csrf_token=CNr_U36JufpaLA8R6x3M7GkU; passport_fe_beating_status=true; R6kq3TV7=AE2gMlx6AQAAvYTIxl1fM6CJucIyAsBAUzGr4wnMSMq_6yiMDSgTUmhFcSbf|1|0|b3a2973dfcb43ae52d9d00e9277d1a6322c89558; csrf_session_id=fa5fdc18618e46b194f075f56bcae4bb; bm_sz=F0C984664CBD3F98CB69CC3A5D7311D7~YAAQdjNWslxzzyN6AQAAD7cyXAxHYhY8U5I2hd7pyliCaDNgsuAGvrdk20NPdnHcCgfuoQ4jTt9grk2oytGVbW5tLSYfrhXY3YvP1QNF6aamZaoqmem4EdYBQ9MB7WwprJmH3VhLP8rA8oNNKWu+kcnyP7wPW1zIWDsNXzUn0xo6rVLuPi7SqZI2wES/OECk; ak_bmsc=FAB809A889BE0FD52793A9AFE944C5E7~000000000000000000000000000000~YAAQdjNWsl5zzyN6AQAAD7cyXAyCowossZhpYTS17Hr59PNFrcXTcDFryYYdokg3LpNXsgKzh1XPNtNyQPIaBpTObs+sRSYDommrQqfkj+rmJXmJ9ZgGG9nmz9g+na9QQvlE1WCChZXDfqjafulwVYqiREPUGZOOYZQR+VFcscgiEIDX8Sf/oVd4y/DFai5cVmE+NdFv8mScSPqrnx7GN6aRjgNcH1U4AH2s5rDsXx8HFPeAx3Tv+GnXIe+LW4VkayVwC0jmsc/5ItiIBg/frNY6TGlhMC2GpkC/5r3kusXk7pGrOZ3guS4XutcnrywaEVBJ2mAT4HZMO4BGWGdQKuewF2jloIzCXLIMrEZZH/cn5YpzHY2bSMAOMcn5i2LGSnbgBwd5Gepl; bm_sv=DEBE6CA7A7EB283E553319561E46F9DD~RZAdeW6TH0kHw11O3hwiJna+CzGbn2Uq0XJUyTGiSWUjhw3nZNKxa7ykll7CbirsQfI9gqLMNlqF/UxaDjD2dEqXktEXKFSM7Bc850t9Kj8Q3Y3pX0/GQSdjYx0/15QSfNX8ueYzHrsYeiYz9ZXmGe+OUh1uYKw8zShfTUs4pBQ=; s_v_web_id=verify_kqj9kjg8_h6I0T7wu_Rewg_4N6a_ANgb_RwrZSHwKIbIO',
        'Content-Length': '0', }
    while True:
        time.sleep(6.6)
        req=requests.post(url, headers=headers)
        if '"تم إرسال التعليق بنجاح"' in req.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            done+=1
        elif 'أنت تعلق بسرعة كبيرة. خذ قسطًا من الراحة!' in req.text:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            error+=1
        elif 'انتهت صلاحية تسجيل الدخول' in req.text:
            print(f'\n\t[⚠] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗲𝘅𝗽𝗶𝗿𝗲𝗱\nsession id [{sid1}]')
            sessid2()
            break
        elif '{}' in req.text:
            print(f'\n\t[🛑] 𝗬𝗼𝘂𝗿 𝘀𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗗 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗯𝗮𝗻𝗻𝗲𝗱\nsession id [{sid1}]')
            sessid2()
            break
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}Done comment [{done}]{Fore.RESET} | {Fore.RED}Error comment [{error}]{Fore.RESET} | {Fore.CYAN}Post id: [{postid}] Text [{tx}] {Fore.RESET}',end='')
            error+=1
def start():
    print("""
              Spam comments
     _____ _ _      _____     _    
    |_   _(_) | __ |_   _|__ | | __
      | | | | |/ /   | |/ _ \| |/ /
      | | | |   <    | | (_) |   < 
      |_| |_|_|\_\   |_|\___/|_|\_/""")
    print("By @TweakPY _ @Filza2")
    print("=====================================")
    TweakPY=input("Enter any key to start...\n")
    print('')
    if TweakPY=="":
        sessid1()
    else:
        sessid1()
start()