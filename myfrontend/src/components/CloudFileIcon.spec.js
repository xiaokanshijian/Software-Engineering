import { shallowMount } from '@vue/test-utils';
import CloudFileIcon from './CloudFileIcon.vue';





describe('<CloudFileIcon/>', () => {
	const wrapper = shallowMount(CloudFileIcon);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(CloudFileIcon);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

