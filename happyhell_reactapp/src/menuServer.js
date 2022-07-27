import axios from "axios"

const API_URL = "http://192.168.88.103:8080/api/empresa"

export const menu = async () => {
    return await fetch(API_URL)
}