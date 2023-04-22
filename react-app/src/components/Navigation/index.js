import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
    <ul className="navbar">
      <li>
        <NavLink className="home-link" exact to="/">
          <i class="fa-solid fa-p"></i>
          <i class="fa-solid fa-a"></i>
          <i class="fa-solid fa-l"></i>
          <i class="fa-solid fa-e"></i>
          <i class="fa-solid fa-egg"></i>
          <i class="fa-solid fa-p"></i>
          <i class="fa-solid fa-e"></i>
          <i class="fa-solid fa-t"></i>
          <i class="fa-solid fa-s"></i>
          {/* <i class="fa-solid fa-exclamation"></i> */}
        </NavLink>
      </li>
      {isLoaded && (
        <li>
          <ProfileButton user={sessionUser} />
        </li>
      )}
    </ul>
  );
}

export default Navigation;