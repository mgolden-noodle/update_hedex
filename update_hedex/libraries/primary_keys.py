class PrimaryKeys(object):
    primary_keys = {
        "Retention_Catalog_Terms": {
            "terms": {
                "_": [
                    [("termCode",), ("sessionCode", "string", None)]
                ]
            }
        },
        
        "Retention_Catalog_Sections": {
            "sections": {
                "_": [
                    [("sisSectionId",)],
                    [("lmsSectionId",)],
                    [("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("termCode",), ("sectionRefNum",)],
                ]
            }
        },
        
        "Retention_FacultyStaff_Staff": {
            "retentionPersons": {
                "_": [
                    [("personSisId",)],
                    [("personLmsId",)]
                ],
                "alternateIDs": {
                    "_": [
                        [("personAlternateIdType",)]
                    ]
                },
                "PersonAddresses": {
                    "_": [
                        [("addressType",), ("addressStartDate", "date", None), ("addressEndDate", "date", None)]
                    ]
                },
                "PersonPhones": {
                    "_": [
                        [("phoneType",)]
                    ]
                },
                "PersonEmails": {
                    "_": [
                        [("emailAddressType",)]
                    ]
                }
            }
        },

        "Retention_FacultyStaff_AdvisingRelationship": {
            "advisors": {
                "_": [
                    [("advrId",), ("studentId",), ("advrTermCode",), ("advrType", "string", None)]
                ]
            }
        },
        
        "Retention_FacultyStaff_Teaching": {
            "teaching": {
                "_": [
                    [("personSisId",), ("sisSectionId",)],
                    [("personLmsId",), ("sisSectionId",)],
                    [("personSisId",), ("lmsSectionId",)],
                    [("personLmsId",), ("lmsSectionId",)],
                    [("personSisId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personLmsId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personSisId",), ("termCode",), ("sectionRefNum",)],
                    [("personLmsId",), ("termCode",), ("sectionRefNum",)]
                ]
            }
        },
        
        "Retention_StudentRecords_Students": {
            "retentionPersons": {
                "_": [
                    [("personSisId",)],
                    [("personLmsId",)]
                ],
                "alternateIDs": {
                    "_": [
                        [("personAlternateIdType",)]
                    ]
                },
                "PersonAddresses": {
                    "_": [
                        [("addressType",), ("addressStartDate", "date", None), ("addressEndDate", "date", None)]
                    ]
                },
                "PersonPhones": {
                    "_": [
                        [("phoneType",)]
                    ]
                },
                "PersonEmails": {
                    "_": [
                        [("emailAddressType",)]
                    ]
                },
                "studentTermItems": {
                    "_": [
                        [("termCode",)]
                    ]
                }
            }
        },
        
        "Retention_StudentRecords_StudentEnrollments": {
            "studentEnrollments": {
                "_": [
                    [("personSisId",), ("sisSectionId",)],
                    [("personLmsId",), ("sisSectionId",)],
                    [("personSisId",), ("lmsSectionId",)],
                    [("personLmsId",), ("lmsSectionId",)],
                    [("personSisId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personLmsId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personSisId",), ("termCode",), ("sectionRefNum",)],
                    [("personLmsId",), ("termCode",), ("sectionRefNum",)]
                ]
            }
        },

        "Retention_Engagement_Attendance": {
            "attendance": {
                "_": [
                    [("personSisId",), ("sisSectionId",)],
                    [("personLmsId",), ("sisSectionId",)],
                    [("personSisId",), ("lmsSectionId",)],
                    [("personLmsId",), ("lmsSectionId",)],
                    [("personSisId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personLmsId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personSisId",), ("termCode",), ("sectionRefNum",)],
                    [("personLmsId",), ("termCode",), ("sectionRefNum",)]
                ]
            }
        },
        
        "Retention_Engagement_Assignments": {
            "assignments": {
                "_": [
                    [("personSisId",), ("sisSectionId",), ("assignmentLmsId",)],
                    [("personLmsId",), ("sisSectionId",), ("assignmentLmsId",)],
                    [("personSisId",), ("lmsSectionId",), ("assignmentLmsId",)],
                    [("personLmsId",), ("lmsSectionId",), ("assignmentLmsId",)],
                    [("personSisId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",), ("assignmentLmsId",)],
                    [("personLmsId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",), ("assignmentLmsId",)],
                    [("personSisId",), ("termCode",), ("sectionRefNum",), ("assignmentLmsId",)],
                    [("personLmsId",), ("termCode",), ("sectionRefNum",), ("assignmentLmsId",)]
                ]
            }
        },
        
        "Retention_Engagement_EngagementActivity": {
            "engagementActivity": {
                "_": [
                    [("personSisId",), ("sisSectionId",)],
                    [("personLmsId",), ("sisSectionId",)],
                    [("personSisId",), ("lmsSectionId",)],
                    [("personLmsId",), ("lmsSectionId",)],
                    [("personSisId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personLmsId",), ("termCode",), ("sessionCode", "string", None), ("subjectCode",), ("sectionCourseNumber",), ("sectionNumber",)],
                    [("personSisId",), ("termCode",), ("sectionRefNum",)],
                    [("personLmsId",), ("termCode",), ("sectionRefNum",)]
                ]
            }
        }
        
    }
