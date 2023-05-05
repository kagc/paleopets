const GET_PET = "pets/GET_PET"
const CREATE_PET = "pets/CREATE_PET"
const EDIT_PET = "pets/EDIT_PET"
const LOAD_PETS = "pets/LOAD_PETS"
const USER_PETS = "pets/USER_PETS"


const onePet = (pet) => ({
    type: GET_PET,
    pet
})

const add = (pet) => ({
    type: CREATE_PET,
    pet
})

const edit = (pet) => ({
    type: EDIT_PET,
    pet
})

const allPets = (pets) => ({
    type: LOAD_PETS,
    pets
})

const userPets = (pets) => ({
    type: USER_PETS,
    pets
})