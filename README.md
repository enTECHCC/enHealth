# enHEALTH
An app to consolidate drug information from trusted websites, making it accessible to senior users.

* http://www.mayoclinic.org/
* http://my.clevelandclinic.org/
* https://www.drugs.com/
* https://www.nih.gov/
* https://medlineplus.gov/
* https://www.patientslikeme.com/

## Template for Json output

```json
{
    "GenericName" : "escitalopram",
    "BrandName" : "Cipralex",
    "RecommendedDosage" : "10 mg",
    "Interactions" : [
        "alcohol", "alfuzosin", "amiodarone",
        "anagrelide", "asenapine", "azithromycin",
        "buserelin", "chloroquine", "ciprofloxacin",
        "cimetidine", "clarithromycin", "clozapine",
        "crizotinib", "degarelix"
    ],
    "GeneralDescriptions" : "",
    "SideEffectsList" : ["SE1", "SE2"],
    "SideEffectsParag" : "paragraph on side effects",
    "Usage" : "Paragraph on usage",
    "ActiveIngredients" : ["ingredient1", "ingredient2"],
    "Warnings" : "Warning information",
    "Source" : "www.medical-website.com"
}
```
