import { Layout } from './components/Layout';
import { Flow } from './components/Flow';
import { Toaster } from './components/ui/sonner';

export default function App() {
  return (
    <>
      <Layout>
        <Flow />
      </Layout>
      <Toaster />
    </>
  );
}
