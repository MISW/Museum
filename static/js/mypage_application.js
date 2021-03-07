$(function(){


    //TOP IMAGE 
    $(".image_input_group").each(function(i){
        const new_output=$(this).find(".image_new_output");
        const old_output=$(this).find(".image_old_output");
        const top_image_input=$(this).find("#id_top_image");
        const top_image_clear= $(this).find("#top_image-clear_id");

        //new (add new top image)
        ShowInputImage(top_image_input,new_output);

        //clear (delete old top image)
        top_image_clear.on("change",function(){
            if(top_image_clear.prop('checked')===true){
                old_output.fadeOut()
                console.log("true")
            }else{
                old_output.fadeIn()
                console.log("false")
            }  
        });
    });



    //Media Files
    const media_file_input_num_max=3;
    const media_file_input_area=$("#media_file_input_area");
    const media_file_input_base=$("#media_file_input_base").html()
    $("#media_file_input_base").remove()
    var media_file_input_num_now= media_file_input_area.find(".media_file_input").length;
    $("#media_file_input_num_max").html(media_file_input_num_now+" / "+media_file_input_num_max);
    addEventRemoveMediaForm();

    $('#add_media_file_button').on('click',function(){
        if(media_file_input_num_now==media_file_input_num_max) return;
        media_file_input_num_now++;
        //media_file_input_area.append("<p>【"+media_file_input_num_now+"】</p>"+media_file_input_base);
        media_file_input_area.append(media_file_input_base);
        $("#media_file_input_num_max").html(media_file_input_num_now+" / "+media_file_input_num_max);

        //for remove (clear)
        addEventRemoveMediaForm();
    });

    function addEventRemoveMediaForm(){
        media_file_input_area.find(".media_file_input").each(function(){
            var eles=$(this).find('#remove_media_file_button');
            eles.off();
            eles.on('click',function(){
                if(media_file_input_num_now==0) return;
                media_file_input_num_now--;
                $("#media_file_input_num_max").html(media_file_input_num_now+" / "+media_file_input_num_max);
                const ele=$(this).parents(".media_file_input");
                ele.fadeOut();
                $(this).remove();
                setTimeout(function(){
                    ele.remove();
                },1000);
            });
        });
    }


    
    //Links
    const link_input_num_max=5;
    const link_input_area=$("#link_input_area");
    const link_input_base=$("#link_input_base").html()
    $("#link_input_base").remove()
    var link_input_num_now=link_input_area.find(".link_input").length;;
    $("#link_input_num_max").html(link_input_num_now+" / "+link_input_num_max);
    addEventRemoveLinkForm()
    
    $('#add_link_button').on('click',function(){
        if(link_input_num_now==link_input_num_max) return;
        link_input_num_now++;
        link_input_area.append(link_input_base);
        $("#link_input_num_max").html(link_input_num_now+" / "+link_input_num_max);

        //for remove (clear)
        addEventRemoveLinkForm()
    });

    function addEventRemoveLinkForm(){
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



    //共同作成者
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


    //linkの必要不必要管理  見たらわかるようにele→label→div↓input という厳密な順番でないと使えない
    /*
    function link_required_prop(ele){
        ele.on('change',function(){
            if($(this).prop('checked')){
                console.log(0);
                $(this).next('label').next('div').children('input').prop('required',true);
            }else{
                console.log(1);
                $(this).next('label').next('div').children('input').prop('required',false);
                $(this).next('label').next('div').children('input').val("");//入力を消す
            }
        });
    }
    link_required_prop($("#check0"));
    link_required_prop($("#check1"));
    link_required_prop($("#check2"));
    link_required_prop($("#check3"));
    link_required_prop($("#check4"));
    */




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

function ShowInputImage(input,output){
    input.on("change",function(e){
        if(!e.target.files[0]){
            output.attr('src',"");
            return;
        }
        var reader = new FileReader();
        reader.onload = function (e) {
            output.attr('src', e.target.result);
        }
        reader.readAsDataURL(e.target.files[0]);
    });
}