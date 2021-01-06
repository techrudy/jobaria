import axios from "axios";

export async function checkAuth(token) {
    const { data } = await axios.post(
        "http://localhost:8000/api/",
        {
            query: `
            query CheckAuth {
              checkAuth { 
                success {
                  msg
                  user {
                    id
                    username
                    email
                    first_name
                    last_name
                    company {
                      id
                      name
                      description
                      created_at
                      updated_at
                    }
                    __typename
                  }
                }
                error
              }
            }
          `,
        }, {
        headers: {
            "Authorization": token,
        },
    });

    const user = data.data.checkAuth
    return user
}