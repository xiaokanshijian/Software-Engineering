import { shallowMount } from '@vue/test-utils';
import Header from './Header.vue';





describe('<Header/>', () => {
	const wrapper = shallowMount(Header);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(Header);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

