import { createSlice } from '@reduxjs/toolkit'
import sideBar6 from '../../assets/utils/images/sidebar/city1.jpg';

const initialState = {
    backgroundColor: '',
    headerBackgroundColor: '',
    enableMobileMenuSmall: '',
    enableBackgroundImage: false,
    enableClosedSidebar: false,
    enableFixedHeader: true,
    enableHeaderShadow: true,
    enableSidebarShadow: true,
    enableFixedFooter: true,
    enableFixedSidebar: true,
    colorScheme: 'white',
    backgroundImage: sideBar6,
    backgroundImageOpacity: 'opacity-06',
    enablePageTitleIcon: true,
    enablePageTitleSubheading: true,
    enablePageTabsAlt: true,
}

export const themeOptions = createSlice({
    name: 'ThemeOptions',
    initialState,
    reducers: {
        setEnableBackgroundImage: (state, action) => {
            return {
                ...state,
                enableBackgroundImage: action.payload
            };
        },
        setEnableFixedHeader: (state, action) => {
            return {
                ...state,
                enableFixedHeader: action.payload
            };
        },
        setEnableHeaderShadow: (state, action) => {
            return {
                ...state,
                enableHeaderShadow: action.payload
            };
        },
        setEnableSidebarShadow: (state, action) => {
            return {
                ...state,
                enableSidebarShadow: action.payload
            };
        },
        setEnablePageTitleIcon: (state, action) => {
            return {
                ...state,
                enablePageTitleIcon: action.payload
            };
        },
        setEnablePageTitleSubheading: (state, action) => {
            return {
                ...state,
                enablePageTitleSubheading: action.payload
            };
        },
        setEnablePageTabsAlt: (state, action) => {
            return {
                ...state,
                enablePageTabsAlt: action.payload
            };
        },
        setEnableFixedSidebar: (state, action) => {
            return {
                ...state,
                enableFixedSidebar: action.payload
            };
        },
        setEnableClosedSidebar: (state, action) => {
            return {
                ...state,
                enableClosedSidebar: action.payload
            };
        },
        setEnableMobileMenu: (state, action) => {
            return {
                ...state,
                enableMobileMenu: action.payload
            };
        },
        setEnableMobileMenuSmall: (state, action) => {
            return {
                ...state,
                enableMobileMenuSmall: action.payload
            };
        },
        setEnableFixedFooter: (state, action) => {
            return {
                ...state,
                enableFixedFooter: action.payload
            };
        },
        setBackgroundColor: (state, action) => {
            return {
                ...state,
                backgroundColor: action.payload
            };
        },
        setHeaderBackgroundColor: (state, action) => {
            return {
                ...state,
                headerBackgroundColor: action.payload
            };
        },
        setColorScheme: (state, action) => {
            return {
                ...state,
                colorScheme: action.payload
            };
        },
        setBackgroundImageOpacity: (state, action) => {
            return {
                ...state,
                backgroundImageOpacity: action.payload
            };
        },
        setBackgroundImage: (state, action) => {
            return {
                ...state,
                backgroundImage: action.payload
            };
        }
    },
})

// Action creators are generated for each case reducer function
export const {
    setEnableBackgroundImage,
    setEnableFixedHeader,
    setEnableHeaderShadow,
    setEnableSidebarShadow,
    setEnablePageTitleIcon,
    setEnablePageTitleSubheading,
    setEnablePageTabsAlt,
    setEnableFixedSidebar,
    setEnableClosedSidebar,
    setEnableMobileMenu,
    setEnableMobileMenuSmall,
    setEnableFixedFooter,
    setBackgroundColor,
    setHeaderBackgroundColor,
    setColorScheme,
    setBackgroundImageOpacity,
    setBackgroundImage
} = themeOptions.actions

export default themeOptions.reducer