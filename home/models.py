from _decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

country = ["Afghanistan", "Åland Islands", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla",
           "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas",
           "Bahrain", "Bangladesh", "Barbados", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
           "Bosnia and Herzegovina", "Botswana", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam",
           "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands",
           "Central African Republic", "Chad", "Chile", "China", "Cocos (Keeling) Islands", "Colombia", "Comoros",
           "Congo", "Democratic Republic of the Congo", "Cook Islands", "Costa Rica", "Côte d'Ivoire", "Croatia",
           "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
           "El Salvador", "Eritrea", "Estonia", "Ethiopia", "Faeroe Islands", "Fiji", "Finland", "France",
           "French Guiana", "French Polynesia", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece",
           "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana",
           "Haiti", "Holy See", "Honduras", "Hong Kong Special Administrative Region of China", "Hungary", "Iceland",
           "India", "Indonesia", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey",
           "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Republic of Korea", "Kuwait", "Kyrgyzstan",
           "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya",
           "Liechtenstein", "Lithuania", "Luxembourg", "Macao Special Administrative Region of China",
           "The former Yugoslav Republic of Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta",
           "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
           "Micronesia, Federated States of", "Republic of Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat",
           "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia",
           "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norfolk Island", "Northern Mariana Islands", "Norway",
           "Oman", "Pakistan", "Palau", "Occupied Palestinian Territory", "Panama", "Papua New Guinea", "Paraguay",
           "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Réunion", "Romania", "Rwanda",
           "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",
           "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
           "Slovakia", "Slovenia", "Solomon Islands", "South Africa", "Spain", "Sri Lanka", "Suriname",
           "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Taiwan, Province of China",
           "Tajikistan", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
           "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "United Arab Emirates",
           "United Kingdom of Great Britain and Northern Ireland", "United States of America",
           "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu",
           "Venezuela (Bolivarian Republic of)", "Viet Nam", "British Virgin Islands", "United States Virgin Islands",
           "Wallis and Futuna Islands", "Yemen", "Zambia", "Zimbabwe",
           ]


# to store the delivery address
class Address(models.Model):
    user = models.ForeignKey('auth_login.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100, choices=[(country, country) for country in country], default="India")
    phone_number = models.CharField(max_length=10, validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return self.address
