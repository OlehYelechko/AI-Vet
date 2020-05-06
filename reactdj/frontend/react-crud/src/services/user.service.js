import http from "../http-common";
class UserDataService {
    create(data){
        return http.post("/rest-auth/registration/", data);
    }

}

export default new UserDataService();