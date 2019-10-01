stop_words = (
    "a,about,above,across,after,again,against,all,allmost,alone,along,already,also,although,always,am,among,amount,an,and,another,any,are,around,"
    "as,at,back,be,because,been,but,before,behind,being,between,beyond,bill,by,can,could,cry,detail,do,does,down,due,during,each,eight,either,eleven,else,empty,"
    "etc,ever,every,except,few,fifteen,fifty,find,fire,first,five,for,forty,four,from,front,full,further,get,give,go,had,has,have,he,her,herself,here,"
    "himself,his,how,however,hundred,if,in,inc,indeed,into,is,it,it's,its,itself,keep,last,latter,least,less,ltd,many,may,me,meanwhile,might,mill,mine,more,"
    "moreover,most,much,must,my,myself,name,neither,never,nevertheress,next,nine,no,nobody,none,noone,nor,not,nothing,now,of,off,often,on,once,one,only,"
    "or,other,others,otherwise,our,ours,ourselves,out,over,own,part,per,perhaps,please,rather,re,same,seem,seemed,seeming,seems,serious,several,she,should"
    "show,side,since,sincere,six,sixty,so,some,somehow,someone,something,sometime,sometimes,somewhere,still,such,system,take,ten,than,that,the,their,them,"
    "themselves,then,there,thereby,therefore,these,they,thick,thin,third,this,those,though,three,through,throughout,thus,to,together,too,top,toward,towaeds,"
    "twelve,twenty,two,under,until,up,upon,us,very,via,was,we,well,were,what,whatever,when,whenever,where,wherever,whether,which,while,who,whoever,who,whoever,"
    "whole,whom,whose,why,will,with,within,would,yet,you,your,yours,yourself,yourselves,the,"
    ).lower().split(",")


def stopword(str):
    return str.lower() in stop_words


# print(stopword("a"))
# print(stopword("afdjalfd"))
