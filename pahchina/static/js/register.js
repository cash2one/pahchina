// Generated by CoffeeScript 1.7.1
(function() {
  var form_alert, form_success;

  $(document).ready(function() {
    var i, k, p_list, v, _i, _len, _results;
    p_list = location.search.substring(1).split("&");
    _results = [];
    for (_i = 0, _len = p_list.length; _i < _len; _i++) {
      i = p_list[_i];
      k = i.split("=")[0];
      v = i.split("=")[1];
      if ((v != null) && (k != null)) {
        _results.push(document.getElementById("id_" + k).value = v);
      } else {
        _results.push(void 0);
      }
    }
    return _results;
  });

  form_alert = function(loc, name, content) {
    loc.css("background-color", "rgb(255, 224, 219)");
    loc.after("&nbsp;<span id='alert_" + name + "' style='color: red;'>" + content + "</span>");
    return $('input[type="submit"]').attr('disabled', 'disabled');
  };

  form_success = function(loc, name, content) {
    loc.css("background-color", "rgb(147, 236, 147)");
    loc.after("&nbsp;<span id='alert_" + name + "' style='color: green;'>" + content + "</span>");
    return $('input[type="submit"]').removeAttr('disabled');
  };

  $(document).ready(function() {
    var email, username;
    username = $("#id_username");
    username.blur(function() {
      if (username.val() != null) {
        return $.getJSON("/accounts/register/username/" + (username.val()) + "/", function(data) {
          return $.each(data, function(i, field) {
            if (field === false) {
              return form_alert(username, 'username', "用户名已被占用！");
            } else {
              return form_success(username, 'username', '用户名可以使用');
            }
          });
        });
      }
    });
    $("#id_username").focus(function() {
      $(this).css("background-color", "#fff");
      return $("#alert_username").remove();
    });
    email = $("#id_email");
    email.blur(function() {
      var reg;
      if (email.val() != null) {
        reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$/;
        if (reg.test(email.val()) === false) {
          return form_alert(email, 'email', "邮箱格式错误！");
        } else {
          return $.post("/accounts/register/email/", {
            "email": email.val()
          }, function(data) {
            return $.each(data, function(i, field) {
              if (field === false) {
                return form_alert(email, 'email', "该邮箱已被注册！");
              } else {
                return form_success(email, 'email', '该邮箱可以注册！');
              }
            });
          });
        }
      }
    });
    $('#id_email').focus(function() {
      $(this).css("background-color", "#fff");
      return $("#alert_email").remove();
    });
    $('#id_password2').blur(function() {
      if ($("#id_password1").val() !== $(this).val()) {
        return form_alert($(this), "password2", "两次输入的密码不相同！");
      } else {
        return form_success($(this), "password2", "通过！");
      }
    });
    return $('#id_password2').focus(function() {
      $(this).css("background-color", "#fff");
      return $("#alert_password2").remove();
    });
  });

}).call(this);

//# sourceMappingURL=register.map
