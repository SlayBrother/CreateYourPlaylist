"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Name", validators=[InputRequired(), Length(min=1, max=50)]) 
    description = StringField("Description", validators=[InputRequired(), Length(max=55)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Title", validators=[InputRequired(), Length(min=1, max=100)]) 
    artist = StringField("Artist", validators=[InputRequired(), Length(max=55)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
