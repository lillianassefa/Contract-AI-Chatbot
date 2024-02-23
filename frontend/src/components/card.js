import { Box } from '@mui/material'

const Card = (props) => {
  return (
    <Box
      sx={{
        width: '100%',
        height: '300px',
        padding: '10px',
        borderRadius: '10px',
        background: '#BEC8F5',
      }}
    >
      {props.children}
    </Box>
  )
}
export default Card
