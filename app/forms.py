from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class RequestForm(FlaskForm):
    states = [('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
              ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
              ('DC', 'Washington D.C.'), ('DE', 'Delaware'), ('FL', 'Florida'),
              ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'),
              ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
              ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
              ('MA', 'Massachusettes'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
              ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'),
              ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
              ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
              ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
              ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
              ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
              ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'),
              ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'),
              ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), 
              ('WY', 'Wyoming')]
    results_url = StringField('URL', validators=[DataRequired()])
    state_list = SelectMultipleField('States', choices=states)
    submit = SubmitField('Get Results')
