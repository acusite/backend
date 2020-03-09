function createTeam() {
    const team_name = document.getElementById('Team Name')
    const team_leader_name = document.getElementById('Leader Name')
    const team_leader_mail = document.getElementById('Team Leader mail')
    const roll_number1 = document.getElementById('Roll Number')
    const college_name = document.getElementById('College Name')
    const contact = document.getElementById('Contact Number')

    const roll_number2 = document.getElementById('Roll Number1')
    const member2_name = document.getElementById('Team Member1')
    const roll_number3 = document.getElementById('Roll Number2')
    const member3_name = document.getElementById('Team Member2')
    const roll_number4 = document.getElementById('Roll Number3')
    const member4_name = document.getElementById('Team Member3')
    let slug = " "

    axios.post('http://localhost:8000/acuthon/team/',{
            "name" : team_name.value,
            "college" : college_name.value,
        }
    )
    .then(res => {
        console.log(res)
        slug = res.data.slug
        axios.post(`http://localhost:8000/acuthon/register/?team=${res.data.slug}`, {
            "member" : team_leader_name.value,
            "email" : team_leader_mail.value,
            "contact" : contact.value,
            "rollnumber" : roll_number1.value,
        })
        .then(response1 => {
            console.log(response1)
            if (roll_number2 !== null && member2_name !== null){
                axios.post(`http://localhost:8000/acuthon/register/?team=${res.data.slug}`, {
                "member" : member2_name.value,
                "email" : " ",
                "contact" : " ",
                "rollnumber" : roll_number2.value,
                })
                .then(response2 => {
                    console.log(response2)
                    if (roll_number3 !== null && member3_name !== null){
                        axios.post(`http://localhost:8000/acuthon/register/?team=${res.data.slug}`, {
                        "member" : member3_name.value,
                        "email" : " ",
                        "contact" : " ",
                        "rollnumber" : roll_number3.value,
                        })
                        .then(response3 => {
                            console.log(response3)
                            if (roll_number4 !== null && member4_name !== null){
                                axios.post(`http://localhost:8000/acuthon/register/?team=${res.data.slug}`, {
                                "member" : member4_name.value,
                                "email" : " ",
                                "contact" : " ",
                                "rollnumber" : roll_number4.value,
                                })
                                .then(response4 => console.log(response4))
                            }
                         })
                         .catch(err3 => {
                            console.log(err3)
                            axios.delete(`http://localhost:8000/acuthon/delete/${slug}/`)
                            .then(res => console.log(res.data))
                        })
                    }
                })
                .catch(err2 => {
                    console.log(err2)
                    axios.delete(`http://localhost:8000/acuthon/delete/${slug}/`)
                    .then(res => console.log(res.data))
                })
            }
        })
        .catch(err1 => {
            console.log(err1)
            axios.delete(`http://localhost:8000/acuthon/delete/${slug}/`)
            .then(res => console.log(res.data))
        })
    })
    .catch(err => {
        console.log(err)
        axios.delete(`http://localhost:8000/acuthon/delete/${slug}/`)
        .then(res => console.log(res.data))
    })
}
