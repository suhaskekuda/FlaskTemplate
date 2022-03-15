//wrapper for post and get request 
jQuery.extend({
  postRequest: function (url, params={}) {
      let result = null;
      $.ajax({
          url: url,
          type: 'POST',
          data: params,
          dataType: 'JSON',
          async: false,
          ifModified: false,
          success: function (data, textstatus, xhr) {
              result = data;
          },
          error: function () {
              result = "null";
          }
      });
      return result;
  },
getRequest: function (url) {
      let result = null;
      $.ajax({
          url: url,
          type: 'GET',
          dataType: 'JSON',
          async: false,
          ifModified: false,
          success: function (data, textstatus, xhr) {
              result = data;
          },
          error: function () {
              result = "null";
          }
      });
      return result;
  }
});

