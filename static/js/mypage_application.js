$(function(){


//TOP IMAGE 
    $(".image_input_group").each(function(i){
        const new_output_area=$(this).find("#new_output_area");
        const old_output_area=$(this).find("#old_output_area");
        const top_image_input=$(this).find("#id_top_image");
        const top_image_clear= $(this).find("#top_image-clear_id");

        //new (add new top image)
        ShowInputImage(top_image_input,new_output_area);

        //clear (delete old top image)
        top_image_clear.on("change",function(){
            if(top_image_clear.prop('checked')===true){
                old_output_area.fadeOut()
                console.log("true")
            }else{
                old_output_area.fadeIn()
                console.log("false")
            }  
        });
    });



//Media Files
    const media_type_set={0:"画像", 1:"音声", 2:"動画", 3:"zip"};
    const media_file_input_num_max=3;
    const media_file_input_area=$("#media_file_input_area");
    const media_file_input_base=$("#media_file_input_base").html()
    $("#media_file_input_base").remove()
    var media_file_input_num_now= media_file_input_area.find(".media_file_input").length;
    $("#media_file_input_num_max").html(media_file_input_num_now+" / "+media_file_input_num_max);
    //event
    media_file_input_area.find(".media_file_input").each(function(){
        addEvent_RemoveMediaFormEvent(this);
        addEvent_MediaFileInputEvent(this);
        addEvent_MediaFileTypeSelectEvent(this);
    });
    
    //add media
    $('#add_media_file_button').on('click',function(){
        if(media_file_input_num_now==media_file_input_num_max) return;
        media_file_input_num_now++;
        media_file_input_area.append(media_file_input_base);
        $("#media_file_input_num_max").html(media_file_input_num_now+" / "+media_file_input_num_max);

        //event
        media_file_input_area.find(".media_file_input").each(function(){
            addEvent_RemoveMediaFormEvent(this);
            addEvent_MediaFileInputEvent(this);
            addEvent_MediaFileTypeSelectEvent(this);
        });
    });

    function addEvent_RemoveMediaFormEvent(t){
    var eles=$(t).find('#remove_media_file_button');
        eles.off();
        eles.on('click',function(){
            if(media_file_input_num_now==0) return;
            media_file_input_num_now--;
            $("#media_file_input_num_max").html(media_file_input_num_now+" / "+media_file_input_num_max);
            const ele=$(t).parents(".media_file_input");
            ele.fadeOut();
            $(t).remove();
            setTimeout(function(){
                ele.remove();
            },1000);
        });
    }
    function addEvent_MediaFileTypeSelectEvent(t){
        var input_type=$(t).find('#id_media_type');
        input_type.off();
        var input_file=$(t).find('#id_file');
        input_type.on('change',function(){
            var v=media_type_set[input_type.val()]?media_type_set[input_type.val()]:"";
            switch(v){
                case "画像":
                    input_file.attr({'accept':'image/*'})
                    break;
                case "音声":
                    input_file.attr({'accept':'audio/*'})
                    break;
                case "動画":
                    input_file.attr({'accept':'video/*'})
                    break;
                case "zip":
                    input_file.attr({'accept':'.zip'})
                    break;
                default: 
                    input_file.attr({'accept':'*'})
                    break;
            }
        });
    }
    function addEvent_MediaFileInputEvent(t){
        var input=$(t).find('#id_file');
        input.off();
        var output=$(t).find("#new_output_area");
        const type=$(t).find("#id_media_type");
        input.on("change",function(e){
            if(!e.target.files[0]){
                output.html("");
                return;
            }
            var reader = new FileReader();
            const url=createObjectURL ? createObjectURL(e.target.files[0]): e.target.result;

            reader.onload = function (e) {
                var ele;
                switch(media_type_set[type.val()]){
                    case "画像":
                        ele=$("<img>").attr({'src': url });
                        break;
                    case "音声":
                        ele=$("<audio>").attr({'src': url, 'controls':true, });
                        break;
                    case "動画":
                        ele=$("<video>").attr({'src': url, 'controls':true, });
                        break;
                    case "zip":
                        break;
                    default: 
                        ele=$("");
                        break;
                }
                output.html(ele);
            }
            reader.readAsDataURL(e.target.files[0]);
        });
    }


    
//Links
    const link_input_num_max=5;
    const link_input_area=$("#link_input_area");
    const link_input_base=$("#link_input_base").html()
    $("#link_input_base").remove()
    var link_input_num_now=link_input_area.find(".link_input").length;;
    $("#link_input_num_max").html(link_input_num_now+" / "+link_input_num_max);
    addEvent_RemoveLinkFormEvent()
    
    $('#add_link_button').on('click',function(){
        if(link_input_num_now==link_input_num_max) return;
        link_input_num_now++;
        link_input_area.append(link_input_base);
        $("#link_input_num_max").html(link_input_num_now+" / "+link_input_num_max);

        //for remove (clear)
        addEvent_RemoveLinkFormEvent()
    });

    function addEvent_RemoveLinkFormEvent(){
        link_input_area.find(".link_input").each(function(){
            var eles=$(this).find('#remove_link_button');
            eles.off();
            eles.on('click',function(){
                if(link_input_num_now==0) return;
                link_input_num_now--;
                $("#link_input_num_max").html(link_input_num_now+" / "+link_input_num_max);
                const ele=$(this).parents(".link_input");
                ele.fadeOut();
                $(this).remove();
                setTimeout(function(){
                    ele.remove();
                },1000);
            });
        });
    }   

//共同作成者 co_developers
    const co_developer_input=$("#co_developer_input");
    const co_developer_add_button=$("#co_developer_add_button");
    const co_developers_output=$("#co_developers_output");
    const co_developer_add_button_assist=$("#co_developer_add_button_assist");
    const developers_ele=$("#developers_area").find(".checkbox");
    const developers_name = new Array(developers_ele.length);
    //developers' name
    developers_ele.each(function(i,ele){
        developers_name[i]=$(ele).find("#id_co_developer_name").text();   
        const checkInput=$(ele).find('input[name="co_developers"]');
        $(ele).remove();
        if(checkInput.prop("checked")==true){
            add_co_developer(i);
        }
    });
    //autocomplete
    co_developer_input.attr({ autocomplete:"on", list: "developers_datalist_id" });
    const datalist=$("<datalist>").attr({ id: "developers_datalist_id" });
    co_developer_input.append(datalist)
    developers_name.forEach(function(v){
        datalist.append( $("<option>").attr({ value: v, }) );
    });
    //add co_developer
    co_developer_add_button.on('click',function(){
        const name=co_developer_input.val();
        for(const i in developers_name){
            if(developers_name[i]==name){
                add_co_developer(i);
                co_developer_add_button_assist.html('<span style="color:blue;">Found user: user name = '+name+'</span>');
                co_developer_input.val("")
                return;
            }
        }
        if(name===""){
            co_developer_add_button_assist.html('<span style="color:red;">Blank: Enter username of co_developer</span>');
        }else{
            co_developer_add_button_assist.html('<span style="color:red;">NotFound: user name = '+name+'</span>');
        }
        
    });
    function add_co_developer(i){
        co_developers_output.append( developers_ele[i] );
        $(developers_ele[i]).find('input[name="co_developers"]').prop("checked",true);
        $(developers_ele[i]).on("change",function(e){
            $(developers_ele[i]).fadeOut();
            setTimeout(function(){
                $(developers_ele[i]).remove();
                $(developers_ele[i]).show();
            },500);
        });
    }


//ページ移動警告 
    $("input").change(function() {
        $(window).on('beforeunload', function(e) {
            return '入力済みデータが失われます。このまま移動しますか？\n申請する場合は「このまま移動する」を押してください。';
        });
    });
    $("button[type=submit]").click(function() {
        $(window).off('beforeunload');
    });
    $("#form_delete").click(function(){
        $(window).off('beforeunload');
    });

   


//formの中身をalertで表示
    $('form').submit(
        //$('#submit').click(
        function(){
            var message="";
            message+="タイトル: "+$("#id_title").val();
            message+="\n説明: "+$("#id_description").val();
            message+="\n作成者: "+$("#createdBy").val();
            message+="\n共同作成者: ";
            $('input[name="co_developers"]:checked').each(function(){
                message+=$(this).next("span").text()+",  ";
            });

            message+="\n研究会： ";
            $('input[name="associations"]:checked').each(function(){
                message+=$(this).next("span").text()+",  ";
            });

            message+="\nみす内のみ公開: ";
            message+=$("#id_is_private").prop("checked")?"限定しない":"限定する";

            message+="\nメディアファイル: "+media_file_input_num_now+"つ";
            message+="\nリンクファイル: "+link_input_num_now+"つ";
            
            message+="\n\nで申請します。";
            alert(message);

        }
    );  
    

});

//入力された画像の出力
function ShowInputImage(input,output){
    input.on("change",function(e){
        if(!e.target.files[0]){
            output.html("");
            return;
        }
        var reader = new FileReader();
        const url=createObjectURL ? createObjectURL(e.target.files[0]): e.target.result;

        reader.onload = function (e) {
            var img=$("<img>").attr({'src': url });
            output.html( img );
        }
        reader.readAsDataURL(e.target.files[0]);
    });
}

var createObjectURL = (window.URL && window.URL.createObjectURL) ? function(file) {
    return window.URL.createObjectURL(file);
} : (window.webkitURL && window.webkitURL.createObjectURL) ? function(file) {
    return window.webkitURL.createObjectURL(file);
} : undefined;