/*
 * @作者: kerwin
 * @公众号: 大前端私房菜
 */
function queryStringify(obj) {
    let str = ''
    for (let k in obj) str += `${k}=${obj[k]}&`  //得到结果username=kerwin&&password=789&
    return str.slice(0, -1)  //把最后的&截掉
  }
  
  // 封装 ajax
  function ajax(options) {
    let defaultoptions = {  //设定一个默认值defaultoption，是防止将来option传入的参数不全出错
      url: "",
      method: "GET", //大小写都生效
      async: true,
      data: {},
      headers: {
        "content-type":"application/x-www-form-urlencoded"
      }, //post/put等要传入值,可以写好默认值以后调用的时候覆盖，也可以不写。
      success: function () { }, //成功的回调函数。不能写完代码之后在ajax封装的代码中执行，因为不同业务场景下不好写，所以这里传了一个函数，这个函数将来被调用。
      error: function () { } //失败的回调函数
    }
    let { url, method, async, data, headers, success, error } = {
      ...defaultoptions, //先展开默认值，再展开传入的参数
      ...options
    }

    // console.log( url, method, async, data, headers, success, error )
  
    // data传入的是json格式对象还是form编码格式
    if (typeof data === 'object' && headers["content-type"]?.indexOf("json") > -1) {
   data = JSON.stringify(data)
    }
    else {
      data = queryStringify(data)
  
    }
    // 如果是 get 请求, 并且有参数, 那么直接组装一下 url 信息
    if (/^get$/i.test(method) && data) url += '?' + data

  
    // 4. 发送请求
    const xhr = new XMLHttpRequest()
    xhr.open(method, url, async)
    xhr.onload = function () {
      if (!/^2\d{2}$/.test(xhr.status)) {
        // console.log(error)
        error(`错误状态码:${xhr.status}`) //回调,error是方法，加上()表示执行。传进来的函数被调用了，就叫回调函数
        return 
      }
      // 执行解析
      //  catch捕获错误
      try {
        let result = JSON.parse(xhr.responseText)
        // let result = JSON.parse("11111&3333")
        success(result)
      } catch (err) {
        error('解析失败 ! 因为后端返回的结果不是 json 格式字符串')
      }
    }
  
    // 设置请求头内的信息，get不发送data，post发送data
    for (let k in headers) xhr.setRequestHeader(k, headers[k])
    if (/^get$/i.test(method)) {
      xhr.send()
    } else {
      xhr.send(data)
    }
  }