import os
import django
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trustin.settings")
django.setup()

from samples.models import Product, TestingParameter
from branches.models import Branch
products = [
    {
      "SNO": 2010,
      "product_name": "Blood Bag",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2011,
      "product_name": "Surgical Gloves as per IS 13422:1992 (Reaffirmed 2013)",
      "description": "Sterile Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2012,
      "product_name": "Surgical Gloves as per IS 4148:1989 (Reaffirmed 2011)",
      "description": "Non-Sterile Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2014,
      "product_name": "Surgical Gloves as per ASTM D 3577",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2015,
      "product_name": "Disposable Surgical Gloves as per EN 455",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2017,
      "product_name": "Disposable Examination Gloves as per EN 455",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2019,
      "product_name": "Female Condoms as per ISO 25841: 2014/WHO UNAIDS 2012",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2020,
      "product_name": "Male condoms as per Schedule R",
      "description": "Male condoms",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2021,
      "product_name": "Intra Uterine Devices - Copper T 380A",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2022,
      "product_name": "Intra Uterine Devices - Cu 375",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2023,
      "product_name": "Intra Uterine Devices - Tubal Ring as per IS 13009:2000 (Reaffirmed 2015)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2025,
      "product_name": "Surgical Sutures - Absorbable",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2026,
      "product_name": "Surgical Suture - Non-Absorbable",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2027,
      "product_name": "Review of Toxicology Reports",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2030,
      "product_name": "Non-Sterile Examination Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2032,
      "product_name": "Quadruple Blood bag system - 450 ml",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2033,
      "product_name": "Examination Gloves",
      "description": "Powder Content",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2034,
      "product_name": "Male Latex Condoms as per ISO 4074:2015",
      "description": "Male Latex Condoms",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2035,
      "product_name": "Blood Bag systems",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2038,
      "product_name": "Surgical Gloves as per EN 455-1",
      "description": "Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2040,
      "product_name": "PVC Granules",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2041,
      "product_name": "Latex Condoms",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2042,
      "product_name": "Sanitary Napkins",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2043,
      "product_name": "Nitrile Gloves as per ASTM D 6319",
      "description": "Nitrile Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2044,
      "product_name": "Sterile Gloves",
      "description": "Sterile Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2045,
      "product_name": "Surgial Sutures - Absorbable (USP 40)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2046,
      "product_name": "Customer Supplied Method",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2047,
      "product_name": "Surgical Gloves as per ASTM D 3578:2005",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2048,
      "product_name": "Chemical analysis",
      "description": "Protein Content , Bio-burden",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2049,
      "product_name": "Natural Latex Male Condoms",
      "description": "Natural Latex Male Condoms as per ISO 11737 - Part 1",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2050,
      "product_name": "Condoms as per Schedule R",
      "description": "Male Latex Condoms as per Schedule R",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2052,
      "product_name": "Nitrile Gloves as per ASTM D 6124",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2053,
      "product_name": "GLOVES",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2054,
      "product_name": "Natural Fibre",
      "description": "Natural Fibre",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2055,
      "product_name": "R & D Sample",
      "description": "B-Amniotic membrane",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2056,
      "product_name": "OTHER MEDICAL DEVICES",
      "description": "MICROPOROUS TAPE",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2057,
      "product_name": "OTHER MEDICAL DEVICES",
      "description": "BLOOD TRANSFUSION SET",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2058,
      "product_name": "Microbial Challenging",
      "description": "Microbial Challenging IP 2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2059,
      "product_name": "OTHER MEDICAL DEVICES",
      "description": "IV SET",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2060,
      "product_name": "RUBBER STOPPERS",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2061,
      "product_name": "Male Condoms",
      "description": "Male Condoms",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2062,
      "product_name": "Nitrile Gloves",
      "description": "Nitrile Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2063,
      "product_name": "Nitrile Flock lined Gloves",
      "description": "Nitrile Flock lined Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2064,
      "product_name": "Nitrile Flock lined Gloves",
      "description": "Tensile Properties (Before ageing)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2065,
      "product_name": "IP 2018",
      "description": "1.Sodium Bi phosphate, 2.Total Citrate, 3.Dextrose, 4.Total Sodium, 5.Citric Acid",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2066,
      "product_name": "Surgical Gloves As per ISO 10282:2014",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2067,
      "product_name": "Tissue Sample _ TAS/QAD/EXT/062",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2068,
      "product_name": "UNFPA/WHO 2016",
      "description": "Copper T 380A",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2070,
      "product_name": "IQ Wave Logo wrapper",
      "description": "IQ Wave Logo wrapper",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2071,
      "product_name": "IQ Wave probe cover",
      "description": "IQ Wave probe cover",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2072,
      "product_name": "Sterile Latex Surgical Gloves",
      "description": "Sterile Latex Surgical Gloves (Powder Free)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2073,
      "product_name": "Amnion",
      "description": "Amnion",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2074,
      "product_name": 2894243.0001157406,
      "description": "Transfusion Set",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2075,
      "product_name": "Sterile Latex Surgical Glove",
      "description": "Sterile Latex Surgical Glove",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2076,
      "product_name": "Gauze",
      "description": "Gauze",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2077,
      "product_name": "Packing Materials",
      "description": "Validation of Packing Materials",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2078,
      "product_name": "Open Wove Bandage (TYPE 3)",
      "description": "Open Wove Bandage (TYPE 3)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2079,
      "product_name": "Blood Transfusion Set",
      "description": "Blood Transfusion Set",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2080,
      "product_name": "Sterile Latex Surgical Gloves",
      "description": "Sterile Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2081,
      "product_name": "Napkin",
      "description": "Sanitary Napkin",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2082,
      "product_name": "Non Sterile Latex Surgical Glove",
      "description": "Non Sterile Latex Surgical Glove",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2083,
      "product_name": "Sterile Latex Surgical Gloves",
      "description": "Sterile Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2084,
      "product_name": "Surgical Gloves as per EN 455 2",
      "description": "Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2085,
      "product_name": "Surgical Gloves as per EN 455-3",
      "description": "Surgical Gloves as per EN 455-3",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2086,
      "product_name": "R & D Sample as per ASTM-D 5712",
      "description": "R & D Sample",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2087,
      "product_name": "Surgical Gloves as per ASTM D 3577",
      "description": "Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2088,
      "product_name": "Surgical Gloves as per ASTM D 6124",
      "description": "Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2089,
      "product_name": "Surgical Gloves as per ASTM D 5712",
      "description": "Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2090,
      "product_name": "Surgical Gloves as per ISO 11737-1",
      "description": "Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2091,
      "product_name": "Lokus Multipurposed as per ASTM F 1980 & ISO 11737-2",
      "description": "Lokus Multipurposed liquid Polyurethanc Foamed Bandage",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2092,
      "product_name": "Lokus Multipurposed as per ISO 11737-2",
      "description": "Lokus Multipurposed liquid Polyurethanc Foamed Bandage",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2093,
      "product_name": "Intraocular Lens",
      "description": "PMMA Intraocular Lens",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2094,
      "product_name": "Intraocular Lens",
      "description": "Hydrophilic Intraocular Lens",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2095,
      "product_name": "Surgical Gloves as per ISO 11737-2",
      "description": "Surgical Gloves as per ISO 11737-2",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2096,
      "product_name": "Natural Latex Male Condoms",
      "description": "Natural Latex Male Condoms as per ASTM D 5712 - 15",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2097,
      "product_name": "Natural Latex Male Condoms",
      "description": "Natural Latex Male Condoms as per ISO 11737 - 1",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2098,
      "product_name": "Packing Materials",
      "description": "Packing Materials",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2099,
      "product_name": "Male Condom as per ISO11737 - 1",
      "description": "ToTal Aerobic Microbial Count",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2100,
      "product_name": "Male Condom as per ISO11737 - 1",
      "description": "Total Fungal Count",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2101,
      "product_name": "Male Condom as per ISO11737 - 1",
      "description": "Staphylococcus aureus",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2102,
      "product_name": "Male Condom as per ISO11737 - 1",
      "description": "Presence or absent of E.Coli",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2103,
      "product_name": "Male Condom as per ISO11737 - 1",
      "description": "Pseudomonas Aeruginosa",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2104,
      "product_name": "Male Condom as per ISO11737 - 1",
      "description": "Enterobacteriaceae",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2105,
      "product_name": "Sterile Latex Surgical Gloves",
      "description": "Sterile Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2106,
      "product_name": "Sterile Latex Gynecological Gloves as per ISO10993-5 & 10",
      "description": "Sterile Latex Gynecological Gloves Powder free EO Sterile",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2107,
      "product_name": "Sterile Latex Examination Gloves Powdered as per ISO 10993-5&10",
      "description": "Sterile Latex Examination Gloves Powdered",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2108,
      "product_name": "Sterile Latex Surgical Gloves as per ISO10993 - 7",
      "description": "Sterile Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2109,
      "product_name": "Intraocular Lens ASTM F 88",
      "description": "Hydrophilic Acrylic Foldable Intraocular Lens",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2110,
      "product_name": "Intraocular Lens ASTM F 88",
      "description": "PMMA Intraocular Lens",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2111,
      "product_name": "Latex Surgical Gloves as per FTIR",
      "description": "Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2112,
      "product_name": "Latex Surgical Gloves as per ASTM D 3677",
      "description": "Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2113,
      "product_name": "Examination Gloves",
      "description": "Freedom from holes",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2114,
      "product_name": "Examination Gloves",
      "description": "Dimension (Length,Width)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2115,
      "product_name": "Examination Gloves",
      "description": "Thickness",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2116,
      "product_name": "Examination Gloves",
      "description": "Physical Properties - Before & After Ageing",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2117,
      "product_name": "Sterile Latex Surgical Gloves",
      "description": "Residual Eto (Ethylene Oxide, Ethylene Chlorohydrin & Ethylene Glycol)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2118,
      "product_name": "Monofilament Polypropypene Mesh",
      "description": "Non-Absorbsble Surgical Mesh, Sterile Polypropylene mesh",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2119,
      "product_name": "Microbiology Pharma",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2120,
      "product_name": "Microbiology Medical Device",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2121,
      "product_name": "ORS,Oral Rehydration Salt IP",
      "description": "ORS,Oral Rehydration Salt IP 2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2122,
      "product_name": "Paracip 650,Paracetamol Tablets IP",
      "description": "Paracip 650,Paracetamol Tablets IP 2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2123,
      "product_name": "Coldact, Chlorpheniramine Maleate and Phenylephrine Hydrochloride sustained Release Capsules",
      "description": "Coldact, Chlorpheniramine Maleate and Phenylephrine Hydrochloride sustained Release Capsules IP2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2124,
      "product_name": "Cheston Bromhexine Hydrochloride Guaiphenesin & chloropheniramine Maleate Svruo-60ml",
      "description": "Cheston Bromhexine Hydrochloride Guaiphenesin & chloropheniramine Maleate Svruo-60ml IP2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2125,
      "product_name": "Kamasutra Excite Venilla Flavored condoms",
      "description": "Kamasutra Excite Venilla Flavored condoms ISO 11737-1",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2126,
      "product_name": "Water for Injection",
      "description": "Water for Injection IP2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2127,
      "product_name": "Water for Injection",
      "description": "Water for Injection USP",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2128,
      "product_name": "JMS.IV SET",
      "description": "JMS.IV SET IP2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2129,
      "product_name": "EVE s Copper T 380A/Tcu 380A",
      "description": "EVE s Copper T 380A/Tcu 380A IP2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2130,
      "product_name": "Catheter",
      "description": "Catheter",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2131,
      "product_name": "Gentamicin Eye Drops IP",
      "description": "Gentamicin Eye Drops IP2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2132,
      "product_name": "TUBAL RING",
      "description": "TUBAL RING ISO 13009:2000",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2133,
      "product_name": "Water for Injection",
      "description": "Water for Injection USP",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2134,
      "product_name": "Surgicare Neuro",
      "description": "Surgicare Neuro as per ISO 10993-11",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2135,
      "product_name": "Condoms",
      "description": "Male Condoms",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2136,
      "product_name": "Tri Prep Kit",
      "description": "R & D Sample",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2137,
      "product_name": "Lidocaina 2% Solucion 10ml Inyectable",
      "description": "Lidocaina 2% Solucion 10ml Inyectable",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2138,
      "product_name": "Ciproflloxacina Intusion 100ml",
      "description": "Ciproflloxacina Intusion 100ml",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2139,
      "product_name": "Metilprednisolona Succinato",
      "description": "Metilprednisolona Succinato",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2140,
      "product_name": "Heating exchanger Tube (HET)",
      "description": "Heating exchanger Tube (HET)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2141,
      "product_name": "Re-usable (PMP R-18 Grade) Connectors used in re-usable breathing circits",
      "description": "Re-usable (PMP R-18 Grade) Connectors used in re-usable breathing circits",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2142,
      "product_name": "Blood Bag",
      "description": "Blood Bag",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2143,
      "product_name": "Latex Surgical Gloves As per ISO 11737-1",
      "description": "Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2144,
      "product_name": "Contact plate method as per USP",
      "description": "USP",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2145,
      "product_name": "Wound Dressing As Per ISO11737 - 1",
      "description": "Wound Dressing",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2146,
      "product_name": "Intraocular Lans As per ISO 11737-2:2019",
      "description": "Intraocular Lans",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2148,
      "product_name": "Curcumin in Collagen Base as per ISO 10993-5 &10",
      "description": "Curcumin in Collagen Base",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2149,
      "product_name": "Latex Surgical Gloves - EN 455-3",
      "description": "Latex Surgical Gloves As per EN 455-3",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2150,
      "product_name": "USP",
      "description": "USP (BET)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2151,
      "product_name": "USP",
      "description": "IP/USP Sterility",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2152,
      "product_name": "Reuseable Mask as per ISO 11737 - 1",
      "description": "Reuseable Mask",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2153,
      "product_name": "Purified Water (Millipore Filteration)",
      "description": "Purified Water (Millipore Filteration)",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2154,
      "product_name": "Purified Water",
      "description": "Millipore Filteration",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2155,
      "product_name": "Latex Examination Non-Sterile Gloves As per ASTM D 3578-2005",
      "description": "Latex Examination Non-Sterile Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2156,
      "product_name": 364119.00011574075,
      "description": "Skore Intimaste Post Play Wipes",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2157,
      "product_name": "Krivida Oropharyngeal Flocked Swab",
      "description": "Krivida Oropharyngeal Flocked Swab",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2158,
      "product_name": "HAND WASH",
      "description": "HAND WASH",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2159,
      "product_name": "SANITIZER",
      "description": "SANITIZER",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2160,
      "product_name": "Silicone Male External Catheter-Nusil Silicone",
      "description": "Silicone Male External Catheter-Nusil Silicone",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2161,
      "product_name": "Monopolar Single Stem Cutting TURP Loops",
      "description": "Monopolar Single Stem Cutting TURP Loops",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2162,
      "product_name": "Medical devices - Cirus Breathing Circuit",
      "description": "Medical devices - Cirus Breathing Circuit",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2163,
      "product_name": "ZBOX Electronic Sanitizer",
      "description": "ZBOX Electronic Sanitizer",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2164,
      "product_name": "Diathcrmy Electrodes",
      "description": "Diathcrmy Electrodes",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2165,
      "product_name": "N95 UV Mask",
      "description": "N95 UV Mask",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2166,
      "product_name": "UV Sterilizer",
      "description": "UV Sterilizer",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2167,
      "product_name": "Bioburden Test",
      "description": "Bioburden Test - ISO 11737-1",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2168,
      "product_name": "Sterility Test - ISO 11737-2 / IP 2018",
      "description": "Sterility Test - ISO 11737-2 / IP 2018",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2170,
      "product_name": "Theruptor Barrier Wound Dressing",
      "description": "Theruptor Barrier Wound Dressing",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2171,
      "product_name": "Morrisons Infusion Set - NV",
      "description": "Morrisons Infusion Set - NV",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2172,
      "product_name": "Anti-Microbial Mouthwash",
      "description": "Anti-Microbial Mouthwash ASTM E 2315",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2173,
      "product_name": "Packaging & Transportation Test",
      "description": "Packaging & Transportation Test as per IS 7028",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2174,
      "product_name": "Sterile Latex Surgical Gloves",
      "description": "Sterile Latex Surgical Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2175,
      "product_name": "Disposable Injector",
      "description": "Disposable Injector As per ISO 10993-7",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2176,
      "product_name": "Neoprep nCov-19 Collection",
      "description": "Neoprep nCov-19 Collection",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2177,
      "product_name": "Disinfectant",
      "description": "Disinfectant",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2178,
      "product_name": "First Aid Kit Material",
      "description": "First Aid Kit Material",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2179,
      "product_name": "Sterile Latex Gynaecological Gloves",
      "description": "Sterile Latex Gynaecological Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2180,
      "product_name": "V-PURE WATER",
      "description": "V-PURE WATER",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2181,
      "product_name": "Anti-Microbial Gloves",
      "description": "Anti-Microbial Gloves",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2182,
      "product_name": "TURP Loops",
      "description": "TURP Loops",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2183,
      "product_name": "Needle",
      "description": "Needle",
      "Branch": "Chrompet Branch"
    },
    {
      "SNO": 2184,
      "product_name": "PURE SPERM MEDIA",
      "description": "PURE SPERM MEDIA",
      "Branch": "Chrompet Branch"
    }]
data = [
    {
        "sno": 1,
        "product_name": "Surgical Gloves as per IS 13422:1992 (Reaffirmed 2013)",
        "testing_parameters": "Dimension (mm)",
        "amount": 750,
        "method_specification": "IS 13422 : 1992 (Reaffirmed 2013)",
        "date_of_entry": 43043.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 2,
        "product_name": "Sanitary Napkins",
        "testing_parameters": "Thickness(mm)",
        "amount": 350,
        "method_specification": "IS 5405 : 1980",
        "date_of_entry": 43073.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 3,
        "product_name": "Surgical Gloves as per ASTM D 3578:2005/ASTM D 6124-06",
        "testing_parameters": "Physical Properties - Before ageing",
        "amount": 750,
        "method_specification": "ASTM D 3578:2005",
        "date_of_entry": 43073.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 4,
        "product_name": "Surgical Gloves as per IS 13422:1992 (Reaffirmed 2013)",
        "testing_parameters": "Physical Properties - After ageing (70°C for 168 hrs.)",
        "amount": 5000,
        "method_specification": "IS 13422 : 1992 (Reaffirmed 2013)",
        "date_of_entry": 43073.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 5,
        "product_name": "Surgical Gloves as per IS 13422:1992 (Reaffirmed 2013)",
        "testing_parameters": "Physical Properties - After Ageing (100°C for 22 hrs.)",
        "amount": 1750,
        "method_specification": "IS 13422 : 1992 (Reaffirmed 2013)",
        "date_of_entry": 43073.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 6,
        "product_name": "Surgical Gloves as per IS 13422:1992 (Reaffirmed 2013)",
        "testing_parameters": "Air Tight Test",
        "amount": 750,
        "method_specification": "IS 13422:1992",
        "date_of_entry": 43073.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 7,
        "product_name": "Surgical Gloves as per ASTM D 3577",
        "testing_parameters": "Freedom from Holes",
        "amount": 500,
        "method_specification": "ASTM D 3577",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 8,
        "product_name": "Surgical Gloves as per ASTM D 3577",
        "testing_parameters": "Freedom from Holes",
        "amount": 500,
        "method_specification": "ASTM D 3577",
        "date_of_entry": "18-12-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 9,
        "product_name": "Surgical Gloves as per IS 4148:1989 (Reaffirmed 2011)",
        "testing_parameters": "Thickness (mm)",
        "amount": 750,
        "method_specification": "IS 4148:1989 (Reaffirmed 2011) - Section: 4.3",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 10,
        "product_name": "Surgical Gloves as per IS 4148:1989 (Reaffirmed 2011)",
        "testing_parameters": "Physical Properties - Before ageing",
        "amount": 750,
        "method_specification": "IS 4148:1989 (Reaffirmed 2011) - Section: 4.4.1",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 11,
        "product_name": "Surgical Gloves as per IS 4148:1989 (Reaffirmed 2011)",
        "testing_parameters": "Physical Properties - After ageing (70° for 240 hr)",
        "amount": 5000,
        "method_specification": "IS 4148:1989 (Reaffirmed 2011) - Section: 4.2",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 12,
        "product_name": "Surgical Gloves as per IS 4148:1989 (Reaffirmed 2011)",
        "testing_parameters": "Heat Ageing in Autoclave",
        "amount": 1000,
        "method_specification": "IS 4148 : 1989 (Reaffirmed 2011) - Section: 4.4.3",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 13,
        "product_name": "Surgical Gloves as per IS 4148:1989 (Reaffirmed 2011)",
        "testing_parameters": "pH",
        "amount": 250,
        "method_specification": "IS 4148 : 1989 (Reaffirmed 2011) - Section: 4.4.4",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 14,
        "product_name": "Sanitary Napkins",
        "testing_parameters": "pH",
        "amount": 500,
        "method_specification": "IS 5405 : 1980 (Reaffirmed 2010)",
        "date_of_entry": "13-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 15,
        "product_name": "Male Latex Condoms as per ISO 4074:2015",
        "testing_parameters": "Lubricant Quantity (mg)",
        "amount": 500,
        "method_specification": "WHO UNFPA ISO 4074:2015",
        "date_of_entry": "24-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 16,
        "product_name": "Male Latex Condoms as per ISO 4074:2015",
        "testing_parameters": "Visible Defects",
        "amount": 0,
        "method_specification": "ISO 4074:2015/WHO 2010",
        "date_of_entry": "24-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 17,
        "product_name": "Female Condoms as per ISO 25841: 2014/WHO UNAIDS 2012",
        "testing_parameters": "Burst Volume (Before Ageing) (Lit.)",
        "amount": 1000,
        "method_specification": "ISO 25841- Annex I",
        "date_of_entry": "24-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 18,
        "product_name": "Female Condoms as per ISO 25841: 2014/WHO UNAIDS 2012",
        "testing_parameters": "Burst Pressure (Before Ageing) (KPa)",
        "amount": 1000,
        "method_specification": "ISO 25841- Annex I",
        "date_of_entry": "24-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 19,
        "product_name": "Male Latex Condoms",
        "testing_parameters": "Burst Volume (After Ageing) (Lit.)",
        "amount": 0,
        "method_specification": "ISO 4074:2015/WHO 2010",
        "date_of_entry": "24-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 20,
        "product_name": "Male Latex Condoms",
        "testing_parameters": "Burst Pressure (After Ageing) (KPa)",
        "amount": 0,
        "method_specification": "ISO 4074:2015/WHO 2010",
        "date_of_entry": "24-04-2017",
        "entered_by": "A.MANIVANNAN"
    },
     {
        "sno": 21,
        "product_name": "Review of Toxicology Reports",
        "testing_parameters": "Review of Reports",
        "amount": 0,
        "date_of_entry": "23-11-2017",
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 22,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Polymer Identification Test",
        "amount": 5000,
        "method_specification": "DSC/FTIR/Analytical method",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 23,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Polyglycholic Acid (PGA)",
        "amount": 10000,
        "method_specification": "FTIR+DSC",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 24,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Polydioxanone (PDO)",
        "amount": 10000,
        "method_specification": "FTIR+DSC",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 25,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Material identification - Poliglecaprone (PGA-PCL)",
        "amount": 5000,
        "method_specification": "FTIR only",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 26,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Material identification - Polyglactin 910 (PGA-PLA)",
        "amount": 5000,
        "method_specification": "FTIR only",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 27,
        "product_name": "Quadruple Blood bag system - 450 ml",
        "testing_parameters": "Accelerated ageing study of Quadruple blood bag system - 450 ml",
        "amount": 460000,
        "method_specification": "ISO 3826:2013 & ASTM F 1980/USP",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 28,
        "product_name": "Examination Gloves as per ASTM D 3578",
        "testing_parameters": "Width(mm)",
        "amount": 375,
        "method_specification": "ASTM D3578",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 29,
        "product_name": "Examination Gloves",
        "testing_parameters": "Dimension",
        "amount": 850,
        "method_specification": "ASTM D 3578-2005",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 30,
        "product_name": "Surgical Gloves as per ASTM D 3578:2005/ASTM D 6124-06",
        "testing_parameters": "Thickness",
        "amount": 750,
        "method_specification": "ASTM D3578:2005",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 31,
        "product_name": "Male Latex Condoms",
        "testing_parameters": "In-vitro Cytotoxicity (Qualitative analysis)",
        "amount": 16000,
        "method_specification": "ISO 10993 - Part 5",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 32,
        "product_name": "Male Latex Condoms",
        "testing_parameters": "In-vitro Cytotoxicity by elution method (Quantitative analysis)",
        "amount": 27000,
        "method_specification": "ISO 10993 - Part 5",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 33,
        "product_name": "Curcumin in Collagen Base as per ISO 10993-5 &10",
        "testing_parameters": "Skin Irritation test",
        "amount": 19250,
        "method_specification": "ISO 1099 - 10",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 34,
        "product_name": "Male Latex Condoms",
        "testing_parameters": "Skin Senzitation study (GPMT Method)",
        "amount": 60000,
        "method_specification": "ISO 10993 - Part 10",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 35,
        "product_name": "Wound Dressing As Per ISO11737 - 1",
        "testing_parameters": "Bio-burden test",
        "amount": 2500,
        "method_specification": "ISO 11737-Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 36,
        "product_name": "Male Latex Condoms",
        "testing_parameters": "D. M. Water analysis",
        "amount": 3000,
        "method_specification": "ISO 3696",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 37,
        "product_name": "Blood Bag",
        "testing_parameters": "Emptying under pressure",
        "amount": 800,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 38,
        "product_name": "Blood Bag",
        "testing_parameters": "Rate of collection",
        "amount": 1000,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 39,
        "product_name": "Blood Bag",
        "testing_parameters": "Outlet Port",
        "amount": 250,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 40,
        "product_name": "Blood Bag",
        "testing_parameters": "Collection and Transfer Tube Strength",
        "amount": 400,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
       {
        "sno": 41,
        "product_name": "Blood Bag",
        "testing_parameters": "Blood taking Needle Strength",
        "amount": 500,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 42,
        "product_name": "Blood Bag",
        "testing_parameters": "Suspension",
        "amount": 500,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 43,
        "product_name": "Blood Bag",
        "testing_parameters": "Performance of Labelling",
        "amount": 900,
        "method_specification": "ISO 3826 ;2013 - Part 1",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 44,
        "product_name": "Disposable Surgical Gloves as per EN 455",
        "testing_parameters": "Sterility",
        "amount": 500,
        "method_specification": "IP 2018",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 45,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Material identification - Polyglycholic Acid (PGA)",
        "amount": 10000,
        "method_specification": "FTIR & DSC",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 46,
        "product_name": "Surgical Sutures - Absorbable",
        "testing_parameters": "Material identification - Polydioxanone (PDO)",
        "amount": 10000,
        "method_specification": "FTIR and DSC method",
        "date_of_entry": 42898.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 47,
        "product_name": "Examination Gloves",
        "testing_parameters": "Physical Properties (Tensile Strength (Mpa) and Elongation at Break and Stress at 500% Elongation)",
        "amount": 1000,
        "method_specification": "ASTM D 3578-2005",
        "date_of_entry": 42928.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 48,
        "product_name": "Sterile Gloves",
        "testing_parameters": "Accelerated ageing - Physical Properties (Tensile Strength (Mpa) and Elongation at Break)",
        "amount": 5000,
        "method_specification": "IS 13422 : 1992",
        "date_of_entry": 42928.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 49,
        "product_name": "Sterile Gloves",
        "testing_parameters": "Accelerated ageing Physical Properties (Tensile Strength ( MPa),",
        "amount": 2000,
        "method_specification": "IS 13422:1992",
        "date_of_entry": 42928.00011574074,
        "entered_by": "A.MANIVANNAN"
    },
    {
        "sno": 50,
        "product_name": "Surgical Gloves as per IS 13422:1992 (Reaffirmed 2013)",
        "testing_parameters": "Physical Properties - Before Ageing",
        "amount": 750,
        "method_specification": "IS 13422 : 1992 (Reaffirmed 2013)",
        "date_of_entry": 42928.00011574074,
        "entered_by": "A.MANIVANNAN"
    }
]




branch = Branch.objects.get(pk=1)


for pro in products:
    instance = Product.objects.create(
        branch=branch,
        product_name=pro["product_name"] ,
        description=pro["description"] if pro.get('description') is not None else '',
    )
    for test in data:
        if(test['product_name']== pro['product_name']):

            ins = TestingParameter.objects.create(
                branch=branch,
                product=instance,
                testing_parameters=test["testing_parameters"] ,
                amount=test["amount"],
                method_or_spec=test["method_specification"] if test.get('method_specification') is not None else '',
            )



print("Data added to the database.")