from Domain.MovieValidator import MovieValidator
from Domain.ReservationValidator import ReservationValidator
from Domain.CustomerCardValidator import CustomerCardValidator
from Repository.GenericFileRepository import GenericFileRepository
from Service.MovieService import MovieService
from Service.ReservationService import ReservationService
from Service.CustomerCardService import CustomerCardService
from UserInterface.Console import Console


movie_repository = GenericFileRepository('movies.pkl')
reservation_repository = GenericFileRepository('reservations.pkl')
card_repository = GenericFileRepository('card.pkl')

movie_validator = MovieValidator()
reservation_validator = ReservationValidator()
card_validator = CustomerCardValidator()
undo_list = []
redo_list = []

movie_service = MovieService(movie_repository, reservation_repository, movie_validator, undo_list, redo_list)
reservation_service = ReservationService(reservation_repository, movie_repository, card_repository, reservation_validator, undo_list, redo_list)
customer_card_service = CustomerCardService(card_repository, reservation_repository, card_validator, undo_list, redo_list)

console = Console(movie_service, customer_card_service, reservation_service)
console.run_console()
