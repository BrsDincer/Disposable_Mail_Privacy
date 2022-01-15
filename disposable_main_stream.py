import streamlit as st,requests,json
import random



class CREATOR_MESSAGE():
    def MAIN_PRINT():
        return """
                  
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______I:|      | |  # SUDO        | |             
|:______I:|      | |                | |             
|:______P:|      | |  Privacy is    | |             
|         |      | |  a human right | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       V |      :  '--------------'  :             
|       + |      :'---...______...---'              
|       + |-._.-i___/'             \._              
|'-.____+_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.000000000000000000.'.      :___:
    IIPV      .'.111111111111111111111111.'.         
                 010001100011010001000110
              :____________________________:"""
              
    def SIDE_PRINT():
        return """
    You can use this e-mail to receive disposable messages."""
                                                                                       

class CONFIGURATION_ST():
    def ST_CONF_PARAMETERS():
        conf_st = type("Configuration_Start",(),{"name_panel":"Disposable Mail Privacy",
                                                 "layout_panel":"centered",
                                                 "sitebar_state_panel":"expanded",
                                                 "page_icon":"IIPV"})
        return conf_st()
    def ST_CONFIGURATION_DEFINE():
        Configuration_Function = CONFIGURATION_ST.ST_CONF_PARAMETERS()
        st.set_page_config(Configuration_Function.name_panel,
                           layout=Configuration_Function.layout_panel,
                           initial_sidebar_state=Configuration_Function.sitebar_state_panel,
                           page_icon=Configuration_Function.page_icon)
    

class DEFINE_ST_PARAMETERS():
    def GET_API():
        api_parameters = type("API_PARAMETERS",(),{"tt":st.title,
                                                   "hd":st.header,
                                                   "md":st.markdown,
                                                   "sh":st.subheader,
                                                   "wt":st.write,
                                                   "tx":st.text,
                                                   "ta":st.text_area,
                                                   "c":st.code,
                                                   "cb":st.checkbox})
        info_parameters = type("INFO_PARAMETERS",(),{"i":st.info,
                                                     "w":st.warning,
                                                     "e":st.error,
                                                     "s":st.success})
        return api_parameters,info_parameters

class HTML_TYPE():
    def ST_MARKDOWN_M(text_tar=str):
        return """
<style>
.strin {
        color: black;
        font-size: 22px;
        background-color: rgb(255, 255, 255);
        font-family: Lucida Console;
        padding: 18px 18px 18px;
        letter-spacing: 5px;
        font-weight: bold;
        }        
</style>
<body>
<p class="strin">%s</p>
</body>"""%(text_tar)
    
    def ST_MARKDOWN_SIMPLE(text_tar=str):
        return """
<style>
.strins {
        color: black;
        font-size: 12;
        font-family: Lucida Console;
        background-color: rgb(255, 255, 255);
        padding: 5px 5px 5px;
        }        
</style>
<body>
<p class="strins">%s</p>
</body>"""%(text_tar)
    
    def ST_MARKDOWN_H(text_tar=str):
        return """
<style>
.strinh {
        color: white;
        font-size: 32px;
        font-family: Lucida Console;
        background-color: rgb(0, 0, 0);
        letter-spacing: 5px;
        font-weight: bold;
        }        
</style>
<body>
<p class="strinh">%s</p>
</body>"""%(text_tar)
        


class GET_DOCUMENT():
    def GET_USER_AGENT():
        try:
            list_tar = []
            f_op = open("C:\\Users\\Asus\\Desktop\\user_agent_all.json")
            j_op = json.loads(f_op.read())
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_tar.append(ixlp_values)
            return list_tar
        except:
            pass
        
    def READING_FILE(file_name=str):
        try:
            with open(file_name,"r",errors="replace") as file_tar:
                x_file = []
                for line_x in file_tar:
                    try:
                        ext_tar = line_x.strip()
                        x_file.append(ext_tar)
                    except:
                        pass
            return x_file
        except:
            pass
        
    def GET_HEADER():
        try:
            list_agent = GET_DOCUMENT.GET_USER_AGENT()
            random_agent = random.choice(list_agent)
            ref_ex_list = GET_DOCUMENT.READING_FILE("C:\\Users\\Asus\\Desktop\\ref_list.txt")
            ref_all = random.choice(ref_ex_list)
            date_day = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
            date_month = ["Jan","Feb","Mar","Apr","Aug","Sep","Oct","Nov","Dec"]
            date_day_number = random.randint(1,30)
            date_year = random.randint(2000,2021)
            date_time_x = random.randint(10,23)
            date_time_y = random.randint(10,50)
            date_time_z = random.randint(10,55)
            keep_alive_rate = random.randint(100,155)
            main_header = {"User-Agent":str(random_agent),
                          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                          "Connection":"Keep-Alive",
                          "Keep-Alive":str(keep_alive_rate),
                          "Content-Type":"text/html",
                          "Accept-Encoding":"gzip,deflate",
                          "Accept-Language":"en-us,en;q=0.5",
                          "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                          "Referer":str(ref_all),
                          "Date":f"{random.choice(date_day)}, {date_day_number} {random.choice(date_month)} {date_year} {date_time_x}:{date_time_y}:{date_time_z} GMT"}
            return main_header
        except:
            pass
class SEND_REQUESTS():
    def GET_MAIL():
        req_url = "http://api.guerrillamail.com/ajax.php?f=get_email_address&ip=127.0.0.1&lang=en"
        header_target = GET_DOCUMENT.GET_HEADER()
        r_q = requests.Session()
        get_mail = json.loads(r_q.get(req_url,headers=header_target).text)
        mail_address = get_mail["email_addr"]
        r_q.close()
        return mail_address


class DEFINE_BUTTON():
    def TWO_BUTTON(title_one=str,title_two=str):
        s_t,i_s = DEFINE_ST_PARAMETERS.GET_API()
        s_t.c(CREATOR_MESSAGE.MAIN_PRINT())
        s_t.sh("DISPOSABLE MAIL PRIVACY")
        s_t.md(HTML_TYPE.ST_MARKDOWN_M("GET TEMPORARY E-MAIL"),unsafe_allow_html=True)
        s_t.tx("USE BUTTON TO GET DISPOSABLE MAIL")
        target_get_button = st.button(title_one)
        if target_get_button:
            new_mail = SEND_REQUESTS.GET_MAIL()
            i_s.s("COMPLETED")
            s_t.c(new_mail)
            s_t.tx(CREATOR_MESSAGE.SIDE_PRINT())
        s_t.md(HTML_TYPE.ST_MARKDOWN_M("READ THE MESSAGE"),unsafe_allow_html=True)
        mess_tx = "[>] You can try the button again until the message arrives"
        mess_tx += "\n"
        mess_tx += "[>] Remember that message will be deleted when you read"
        mess_tx += "\n"
        mess_tx += "[>] Transmission of the message may take time"
        s_t.tx(mess_tx)
        user_input = s_t.ta("WRITE YOUR DISPOSABLE MAIL ADDRESS",
                            help="WRITE YOUR DISPOSABLE MAIL ADDRESS").replace(" ","")
        target_read_button=st.button(title_two)
        if target_read_button:
            try:
                cont_before_mail = f"http://api.guerrillamail.com/ajax.php?f=set_email_user&email_user={str(user_input)}"
                check_mail = "http://api.guerrillamail.com/ajax.php?f=check_email&seq=1"
                header_target = GET_DOCUMENT.GET_HEADER()
                r_q = requests.Session()
                r_q.get(cont_before_mail)
                get_mail = json.loads(r_q.get(check_mail,headers=header_target).text)
                mail_id = get_mail['list'][0]['mail_id']
                fetch_mail_on = f"http://api.guerrillamail.com/ajax.php?f=fetch_email&email_id={mail_id}"
                fetch_get = r_q.get(fetch_mail_on)
                fetch_json = json.loads(fetch_get.text)
                s_t.tx("[>] Be sure to save the message before closing or refreshing the page")
                s_t.tx("[>] COMPLETED")
                s_t.tx(f"MAIL FROM: {fetch_json['mail_from']}")
                s_t.tx(f"MAIL SUBJECT: {fetch_json['mail_subject']}")
                s_t.md(fetch_json["mail_body"],
                          unsafe_allow_html=True)
                delete_mail = f"http://api.guerrillamail.com/ajax.php?f=del_email&email_ids[]={mail_id}"
                r_q.get(delete_mail)
                i_s.i("MAIL HAS BEEN DELETED")
                r_q.close()
            except:
                i_s.w("MAIL MAY BE DELETED OR NOT YET AVAILABLE, CHECK LATER")


CONFIGURATION_ST.ST_CONFIGURATION_DEFINE()
DEFINE_BUTTON.TWO_BUTTON("GET NEW DISPOSABLE E-MAIL","READ LAST MESSAGE")
