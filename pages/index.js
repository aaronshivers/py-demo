import Layout from '../components/Layout'
import Link from 'next/link'

const ItemLink = props => (
  <li>
    <Link as={ `/i/${ props.id }` } href={ `/item?title=${ props.title }` }>
      <a>{ props.title }</a>
    </Link>
  </li>
)

export default () => (
  <Layout>
    <h1>Items</h1>
    <ul>
      <ItemLink id="bacon-fries" title="bacon fries" />
      <ItemLink id="hamburger" title="hamburger" />
      <ItemLink id="chicken-fingers" title="chicken fingers" />
    </ul>
  </Layout>
)
