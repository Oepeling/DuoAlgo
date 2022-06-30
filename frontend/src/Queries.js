import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

export function userDataByEmail(user_email) {
    return axios({
        method: 'post',
        url: 'users/profile/email/',
        data: {
            'user_email': user_email,
        },
        headers: {
            'content-type': 'application/json'
        }
    }).then(result => {
        let userData = {}
        if (!result.data.hasOwnProperty('user_data')) {
            console.log('user nu exista')
        } else {
            let data = result.data['user_data'];
            userData = {
                email: result.data['user_data'].email,
                firstName: result.data['user_data'].first_name,
                lastName: result.data['user_data'].last_name,
                phoneNo: data.phone,
                birthday: new Date(data.birthday),
                gender: data.gender
            }
        }

        return userData
    }).catch(function (error) {
        console.log(error)
    })
}

export function userDataById(userId) {
    return axios({
        method: 'post',
        url: 'users/profile/',
        data: {
            'user_id': userId,
        },
        headers: {
            'content-type': 'application/json'
        }
    }).then(result => {
        let userData = {}
        if (!result.data.hasOwnProperty('user_data')) {
            console.log('user nu exista')
        } else {
            let data = result.data['user_data']
            userData = {
                email: data.email,
                firstName: data.first_name,
                lastName: data.last_name,
                phoneNo: data.phone,
                birthday: new Date(data.birthday),
                gender: data.gender
            }
        }

        return userData
    }).catch(function (error) {
        console.log(error)
    })
}

export function updateUser(userData) {
    return axios({
        method: 'post',
        url: 'users/profile/update/',
        data: {
            'user_id': userData.id,
            'user_first_name': userData.firstName,
            'user_last_name': userData.lastName,
            'user_phone': userData.phoneNo,
            'user_birthday': userData.birthday.toISOString().split('T')[0],
            'user_gender': 'N'
        },
        headers: {
            'content-type': 'application/json'
        }
    }).then(result => {
        return result.data['updated']
    }).catch(function (error) {
        console.log(error)
    })
}

export function lessonList() {
    // console.log("!!! query")
    return axios({
        method: 'get',
        url: 'lessons/',
        headers: {
            'content-type': 'application/json'
        }
    }).then(result => {
        let lessons = []
        if (result.data['lesson_list'].empty) {
            console.log('Nu avem lectii :(')
        } else {
            for (let i = 0; i < result.data['lesson_list'].length; i++) {
                let data = result.data['lesson_list'][i]
                let aux_lesson = {
                    id: data.id,
                    title: data.title,
                    author: data.author,
                    stage: data.stage,
                    level: data.level,
                    topic: data.topic,
                    // prerequisites: data.prerequisites,
                    // status: data.status,    // 0 - unavailable, 1 - open, 2 - done
                    status: 1,
                    // lesson: data.lesson,
                    // problems: data.problems,
                }
                lessons.push(aux_lesson)
            }
        }

        return lessons
    }).catch(function (error) {
        console.log(error)
    })
}

export function lessonInfo(lessonId) {
    console.log('lesson/' + lessonId,)
    return axios({
        method: 'get',
        url:  lessonId + '/',
        headers: {
            'content-type': 'application/json'
        }
    }).then(result => {
        let data = result.data['lesson']
        let lesson = {
            id: data.id,
            title: data.title,
            author: data.author,
            stage: data.stage,
            level: data.level,
            topic: data.topic,
            prerequisites: data.dependancies,
            // status: data.status,    // 0 - unavailable, 1 - open, 2 - done
            status: 1,
            content: data.content,
            link_to_code: data.link_to_code,
            tasks: data.tasks,
        }

        return lesson
    }).catch(function (error) {
        console.log(error)
    })
}