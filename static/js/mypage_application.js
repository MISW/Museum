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
    var media_file_input_num={show:[],hide:[]};
    const media_file_input_area=$("#media_file_input_area");
    const media_file_input=media_file_input_area.find(".media_file_input");
    //check if value is already input
    $(media_file_input).each(function(i){
        media_file_input[i].input_id=i;
        if($(media_file_input[i]).find('select[name$="media_type"').val()==""){
            media_file_input[i].initial=false;
            $(media_file_input[i]).hide();
            media_file_input_num.hide.push(i);
        }else{
            media_file_input[i].initial=true;
            $(media_file_input[i]).find("#remove_media_file_button").remove();
            NewMediaTypeFileRelation( $(this).find('select[name$="media_type"]'), $(this).find('input[name$="file"]') );
            media_file_input_num.show.push(i);
            //output
            Output_OldMediaFile(this);
        }
    });
    $("#media_file_input_num_max").html(media_file_input_num.show.length+" / "+(media_file_input_num.show.length+media_file_input_num.hide.length) );
    //event
    media_file_input.each(function(){
        addEvent_RemoveMediaFormEvent(this);
        addEvent_MediaFileInputEvent(this);
        addEvent_MediaFileTypeSelectEvent(this);
    });

    //add media
    $('#add_media_file_button').on('click',function(){
        if(media_file_input_num.hide.length==0) return;
        $(media_file_input[media_file_input_num.hide[0]]).fadeIn();
        media_file_input_area.append( media_file_input[media_file_input_num.hide[0]] );
        media_file_input_num.show.push(media_file_input_num.hide[0]);
        media_file_input_num.hide.splice(0,1);
        $("#media_file_input_num_max").html(media_file_input_num.show.length+" / "+(media_file_input_num.show.length+media_file_input_num.hide.length));
    });
    function addEvent_RemoveMediaFormEvent(t){
    var eles=$(t).find('#remove_media_file_button');
        //eles.off();
        eles.on('click',function(){
            if(media_file_input_num.show.length==0) return;
            $(t).fadeOut();
            clearMediaForm(media_file_input[t.input_id]);
            media_file_input_num.hide.push(t.input_id);
            media_file_input_num.show.splice( media_file_input_num.show.indexOf(t.input_id),1 );
            $("#media_file_input_num_max").html(media_file_input_num.show.length+" / "+(media_file_input_num.show.length+media_file_input_num.hide.length));
        });
    }
    function addEvent_MediaFileTypeSelectEvent(t){
        var input_type=$(t).find('select[name$="media_type"]');
        //input_type.off();
        var input_file=$(t).find('input[name$="file"]');
        input_type.on('change',function(){
            NewMediaTypeFileRelation(input_type,input_file)
        });
    }
    function NewMediaTypeFileRelation(input_type,input_file){
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
    }
    function addEvent_MediaFileInputEvent(t){
        const type=$(t).find('select[name$="media_type"]');
        var input=$(t).find('input[name$="file"]');
        //input.off();
        var output=$(t).find("#new_output_area");
        input.on("change",function(e){
            if(!e.target.files[0]){
                output.html("");
                return;
            }
            var reader = new FileReader();
            const url=createObjectURL ? createObjectURL(e.target.files[0]): e.target.result;
            const name=$(this).prop("files")[0]?$(this).prop("files")[0].name:"";
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
                        ele=$("<a>").attr({'href':url, 'download': name, }).append("<p>"+name+"</p>");
                        break;
                    default: 
                        ele=$('<p style="color:red;">typeを選択してください</p>');
                        break;
                }
                output.html(ele);
            }
            reader.readAsDataURL(e.target.files[0]);
        });
    }
    function Output_OldMediaFile(t){
        const type=media_type_set[$(t).find('select[name$="media_type"]').val()];
        const clear_input=$(t).find('input[name$="file-clear"]');
        const url=$(t).find('a').prop('href');
        var ele;
        switch(type){
            case "画像":
                ele=$("<img>").attr({'src': url, });
                break;
            case "音声":
                ele=$("<audio>").attr({'src': url, 'controls':true, });
                break;
            case "動画":
                ele=$("<video>").attr({'src': url, 'controls':true, });
                break;
            case "zip":
                ele=$("<p>現在zipが登録されています。</p>");
                break;
            default: 
                ele=$('<p style="color:red;">typeを選択してください</p>');
                break;
        };
        const div=$('<div>').attr({'id':'old_output_area'});
        div.append(ele);
        clear_input.next('label').after(div);
        //event
        clear_input.on('change',function(){
            if(clear_input.prop('checked')==true) $(div).fadeOut();
            else $(div).fadeIn();
        });
    }
    function clearMediaForm(t){
        $(t).find('select[name$="media_type"]').val("");
        $(t).find('input[name$="file"]').val("");
        $(t).find("#new_output_area").html("");
    }


    
//Links
    var link_input_num={show:[],hide:[]};
    const link_input_area=$("#link_input_area");
    const link_input=link_input_area.find(".link_input");
    $(link_input).each(function(i){
        link_input[i].input_id=i;
        if($(link_input[i]).find('select[name$="link_type"').val()==""){
            link_input[i].initial=false;
            $(link_input[i]).hide();
            link_input_num.hide.push(i);
        }else{
            link_input[i].initial=true;
            $(link_input[i]).find("#remove_link_button").remove();
            link_input_num.show.push(i);
        }
    });
    $("#link_input_num_max").html(link_input_num.show.length+" / "+(link_input_num.show.length+link_input_num.hide.length));
    link_input.each(function(){
        addEvent_RemoveLinkFormEvent(this);
    });
    
    $('#add_link_button').on('click',function(){
        if(link_input_num.hide.length==0) return;
        $(link_input[link_input_num.hide[0]]).fadeIn();
        link_input_area.append( link_input[link_input_num.hide[0]] );
        link_input_num.show.push( link_input_num.hide[0] );
        link_input_num.hide.splice( 0,1 );
        $("#link_input_num_max").html(link_input_num.show.length+" / "+(link_input_num.show.length+link_input_num.hide.length));
        console.log(link_input_num.show , link_input_num.hide);
    });

    function addEvent_RemoveLinkFormEvent(t){
        var eles=$(t).find('#remove_link_button');
        eles.on('click',function(){
            if(link_input_num.show.length==0) return;
            $(t).fadeOut();
            clearLinkForm(link_input[t.input_id])
            link_input_num.hide.push( t.input_id );
            link_input_num.show.splice( link_input_num.show.indexOf(t.input_id),1 );
            $("#link_input_num_max").html(link_input_num.show.length+" / "+(link_input_num.show.length+link_input_num.hide.length));
            //console.log(link_input_num.show , link_input_num.hide);
            //console.log(t.input_id);
        });
    }   
    function clearLinkForm(t){
        $(t).find('select[name$="link_type"]').val("");
        $(t).find('input[name$="link"]').val("");
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

            message+="\nメディアファイル: "+media_file_input_num.show.length+"つ";
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

