# Group Activity

```
活动状态: status -- 原则是不激活不显示,时间不到不让注册
1:未激活的活动(未来的新活动),默认,添加一个新活动默认为未激活状态,需要人为激活,未激活的活动不会在app段显示,过期的活动会显示。
2:在线活动(当前的活动)
3:下线活动

活动时间状态: time_status -- app端可显示状态
1:未开始活动
2:正在进行中的活动
3:已经过期的活动

注册报名状态:status
1:所有报名;
2:已经添加到我的咨询的报名;
3:未添加到我的咨询的报名

是否注册报名过: is_enrolled
1:注册报名过;
2:没有注册报名过

活动类型: type
1:普通报名
2:整形预约

数据字典解析:
page: 代表第几页,默认为1
size: 代表每页有多少条数据,默认为20
sort: 代表排序方式,默认为create_at

# 测试curl
curl -d '{"page":1,"size":10}' -i https://dev.17mei.cn/v1/activity/list
```

## 获得活动列表 [POST /activity/list]

+ Request

    + Headers

            Token: Optionnal

    + Attributes
        + page: 1 (number)
        + size: 10 (number)
        + sort: sorted by (string)

    + Body

            {
              "page": 1,
              "size": 2,
              "sort": "create_at"
            }

+ Response 200

    + Attributes
        + code: 00000 (string)
        + total: 13 (number)
        + data: object (array)
            + (object)
                + id: activity id (string)
                + time_status: 1 (number)
                + status: 1 (number)
                + num: 1 (number)
                + update_at: 整形时间戳 (number)
                + name: 活动名字 (string)
                + start_at: 整形时间戳 (number)
                + end_at: 整形时间戳 (number)
                + image: 封面图
                + body_parts: 脸部 (array[string]) -- 身体部位
                + type: 1 (number) -- 活动类型

    + Body

            {
              "code": "00000",
              "total": 13,
              "data": [
                {
                  "id": "activity id",
                  "status": 1,
                  "num": 1,
                  "update_at": 0,
                  "title": "活动标题",
                  "start_at": 0,
                  "end_at": 0
                }
              ]
            }


## 获得活动信息 [POST /activity/get]
> short:1--不含content内容;没有short字段时返回包含content的内容

+ Request

    + Headers

            Token: Optionnal

    + Attributes
        + ids: activity id (array)
        + short: 1 (number)

    + Body

            {
              "ids": [
                "activity id"
              ]
            }

+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (array)
            + (object)
                + id: activity id (string)
                + status: 1 (number)
                + time_status: 1 (number)
                + num: 1 (number)
                + update_at: 整形时间戳 (number)
                + start_at: 1234  (number) -- 整形时间戳
                + end_at: 1234  (number) -- 整形时间戳
                + cities: 北京 (array) - 活动城市
                + content: 超文本 (string) - 活动信息
                + body_parts: 脸部 (array[string]) - 身体部位
                + type: 1 (number) -- 活动类型
    + Body

            {
              "code": "00000",
              "data": [
                {
                  "id": "activity id",
                  "status": 1,
                  "num": 1,
                  "update_at": 0,
                  "title": "活动标题",
                  "start_at": 0,
                  "end_at": 0,
                  "name": "美白",
                  "cities": [
                    "北京"
                  ],
                  "content": "超文本",
                  "body_parts": [
                    {
                      "id": 1,
                      "name": "脸部"
                    }
                  ]
                }
              ]
            }

## 活动报名 [POST /activity/enroll]

+ Request

    + Headers

            Token:Required

    + Attributes
        + activity_id: activity id (string)
        + attrs: object (object)
            + nickname: iron (string) - 昵称
            + gender: female (string)  - 性别
            + birthday: `2015-12-24` (string) - 生日
            + occupation: 学生 (string) - 职业
            + body_parts: 脸部 (array[string]) - 身体部位
        + extras: object (object)
            + front_photos: http://qiniu.com/1dasdf/asdf.jpg (array) - 正面照
            + profile_photos: http://qiniu.com/1dasdf/asdf.jpg (array) - 侧面照

    + Body

            {
              "activity_id": "activity id",
              "attrs": {
                "nickname": "iron",
                "gender": "female",
                "birthday": "2015",
                "occupation": "学生",
                "body_parts": [
                  1
                ]
              },
              "extras": {
                "front_photos": [
                  "http://qiniu.com/1dasdf/asdf.jpg"
                ],
                "profile_photos": [
                  "http://qiniu.com/1dasdf/asdf.jpg"
                ]
              }
            }

+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (object)
            + id: 12344 (string) - 活动报名ID

    + Body

            {
              "code": "00000"
            }

## 是否报过名 [POST /activity/is_enrolled]

> 用户是否在该次活动报过名过

+ Request

    + Headers

            Token:Required

    + Attributes
        + activity_id: activity id (string)

    + Body

            {
              "activity_id": "activity id"
            }

+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (object)
            + is_enrolled: 1 (number)
    + Body

            {
              "code": "00000",
              "data": {
                "is_enrolled": 1
              }
            }

## 我的报名列表 [POST /activity/my_enrolled]

+ Request
    + Headers

            Token:Required

    + Attributes
        + page: 1 (number)
        + size: 10 (number)
        + sort: sorted by (string)

    + Body

            {
              "page": 1,
              "size": 2,
              "sort": "create_at",
            }


+ Response 200

    + Attributes
        + code: 00000 (string)
        + total: 13 (number)
        + data: object (array)
            + (object)
                + id: activity id (string)
                + time_status: 1 (number) - 活动时间状态
                + status: 1 (number) - 活动操作状态
                + num: 1 (number)
                + update_at: 整形时间戳 (number)
                + name: 活动名字 (string)
                + start_at: 整形时间戳 (number)
                + end_at: 整形时间戳 (number)
                + image: 封面图
                + body_parts: 脸部 (array[string]) -- 身体部位
                + type: 1 (number) -- 活动类型

  

## 获得报名信息列表 [POST /activity/enroll/list]

+ Request

    + Headers

            Token:Required

    + Attributes
        + activity_id: activity id (string) - 根据活动ID获得活动相关的注册报名
        + page: 1 (number)
        + size: 2 (number)
        + sort: create_at (string)
        + status: 2 (number)
        + mobile: "1234" (string)

    + Body

            {
              "activity_id": "activity id",
              "page": 1,
              "size": 2,
              "sort": "create_at",
              "status": 2,
            }


+ Response 200

    + Attributes
        + code: 00000 (string)
        + total: 2 (number)
        + data: object (array[object])
            + (object)
                + id: enroll_id (string)
                + user_id: user id (string)
                + status: 2 (number)
                + share_count 2 (number)
                + create_at: 11112343 (number)
                + mobile: "86-123" (string)
                + attrs: object (object)
                    + nickname: iron (string) - 昵称
                    + gender: female (string)  - 性别
                    + birthday: `2015-12-24` (string) - 生日
                    + occupation: 学生 (string) - 职业
                    + body_parts: 脸部 (array[string]) - 身体部位

                + extras: object (object)
                    + front_photos: http://qiniu.com/1dasdf/asdf.jpg (array) - 正面照
                    + profile_photos: http://qiniu.com/1dasdf/asdf.jpg (array) - 侧面照

    + Body

            {
              "code": "00000",
              "total": 2,
              "data": [
                {
                  "id": "enroll_id",
                  "user_id": "user_id",
                  "status": 2,
                  "share_count 2": 1,
                  "create_at": 11112343,
                  "mobile": "86",
                  "attrs": {
                    "nickname": "iron",
                    "gender": "female",
                    "birthday": "2015",
                    "occupation": "学生",
                    "body_parts": [
                      "1"
                    ]
                  },
                  "extras": {
                    "front_photos": [
                      "http://qiniu.com/1dasdf/asdf.jpg"
                    ],
                    "profile_photos": [
                      "http://qiniu.com/1dasdf/asdf.jpg"
                    ]
                  }
                }
              ]
            }

## 获得报名详细信息 [POST /activity/enroll/get]

+ Request

    + Headers

            Token:Required

    + Attributes
        + ids: enroll id (array[string])  

    + Body

            {
              "ids": [
                "enroll id"
              ]
            }


+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (array[object])
            + (object)
                + id: enroll_id (string) -
                + user_id: user id (string)
                + activity_id: activity id (string)
                + status: 2 (number)
                + create_at: 11112343 (number)
                + attrs: object (object)
                    + nickname: iron (string) - 昵称
                    + gender: female (string)  - 性别
                    + birthday: `2015-12-24` (string) - 生日
                    + occupation: 学生 (string) - 职业
                    + body_parts: 脸部 (array[string]) - 身体部位

                + extras: object (object)
                    + front_photos: http://qiniu.com/1dasdf/asdf.jpg (array) - 正面照
                    + profile_photos: http://qiniu.com/1dasdf/asdf.jpg (array) - 侧面照

    + Body

            {
              "code": "00000",
              "data": [
                {
                  "id": "enroll_id",
                  "user_id: user_id": "Hello, world!",
                  "activity_id: activity_id": "Hello, world!",
                  "status": 2,
                  "share_count": 2,
                  "create_at": 11112343,
                  "attrs": {
                    "nickname": "iron",
                    "mobile": "86",
                    "gender": "female",
                    "birthday": "2015",
                    "occupation": "学生",
                    "body_parts": [
                      "1"
                    ]
                  },
                  "extras": {
                    "front_photos": [
                      "http://qiniu.com/1dasdf/asdf.jpg"
                    ],
                    "profile_photos": [
                      "http://qiniu.com/1dasdf/asdf.jpg"
                    ]
                  }
                }
              ]
            }

## 创建活动 [POST /activity/add]

+ Request

    + Headers

            Token:Required

    + Attributes
        + start_at: 整形时间戳 (number)
        + end_at: 整形时间戳 (number)
        + name: 美白 (string) - 活动名称
        + cities: 北京 (array) - 活动城市
        + content: 超文本 (string) - 活动信息
        + body_parts: 脸部 (array[string]) - 身体部位
        + image: image url (string)  - 封面
        + type: 1 (number)  - 报名类型 


+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (object)
            + id: 12344 (string) - 活动ID

    + Body

            {
              "code": "00000"
            }

## 活动编辑 [POST /activity/update]

+ Request

    + Headers

            Token:Required

    + Attributes
        + id: activity id (string)
        + start_at: 整形时间戳 (number)
        + end_at: 整形时间戳 (number)
        + name: 美白 (string) - 活动名称
        + cities: 北京 (array) - 活动城市
        + content: 超文本 (string) - 活动信息
        + body_parts: 脸部 (array[string]) - 身体部位
        + image: image url (string)  - 封面
        + status: 1 (number) - 活动状态 


    + Body

            {
              "id": "activity id",
              "title": "活动标题",
              "start_at": 0,
              "end_at": 0,
              "name": "美白",
              "cities": [
                "北京"
              ],
              "content": "超文本",
              "body_parts": [
                {
                  "id": 1,
                  "name": "脸部"
                }
              ]
            }


+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (object)
            + id: 12344 (string) - 活动ID

    + Body

            {
              "code": "00000"
            }



## 修改活动状态 [POST /activity/update_status]

+ Request

    + Headers

            Token:Required

    + Attributes
        + id: activity id (string)
        + status: 2 (number)

    + Body

            {
              "id": "activity id",
              "status": 2
            }

+ Response 200

    + Attributes
        + code: 00000 (string)
        + data: object (object)
            + id: 12344 (string) - 活动ID

    + Body

            {
              "code": "00000"
            }

