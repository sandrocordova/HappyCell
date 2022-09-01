import moment from "moment";

// formatear la fecha tipo 1983-11-23T00:00:00Z a YYYY-MM-DD
export const formatDateZone = (date) => {
    if (!date) return null
    const dateParse = moment.parseZone(date);
    return dateParse.format("YYYY-MM-DD")
}