TELESPHERE="telesphere"
ICORE="icore"
SIMPLESIGNAL="simplesignal"
CUSTOMERPORTAL="customerportal"

ERR_CTG_SECURITY="Security"
ERR_CTG_PARAMETER="Parameter"
ERR_CTG_FUNCTIONAL="Functional"

ERROR = {

    "CDR-002":{
        "code":"CDR-002",
        "value":"You don't have access to this resource",
        "category":ERR_CTG_FUNCTIONAL
    },
    "CDR-003":{
        "code":"CDR-003",
        "value":"Invalid or Missing Parameters",
        "category":ERR_CTG_PARAMETER
    },
    "CDR-001":{
            "code":"CDR-001",
            "value":"Account Not Found",
            "category":ERR_CTG_PARAMETER
     },
    "CDR-006":{
        "code":"CDR-006",
        "value":"Token not found or has expired",
        "category":ERR_CTG_FUNCTIONAL
    },
    "CDR-007":{
        "code":"CDR-007",
        "value":"System Error",
        "category":ERR_CTG_FUNCTIONAL
    },
}